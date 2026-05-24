from choco_coco_brain.settings import (
    ChocoCocoBrainSettings,
    ChocoCocoBrainDefaultBehavor,
)
from choco_coco_brain.pokemon import (
    PokemonAttribute,
)

from pathlib import Path

from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.base.base_query_engine import BaseQueryEngine

from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings as SettingsLLamaIndex,
)

BASES_DIR = Path(__file__).resolve().parent.parent / "bases"


class ChocoCocoBrain:
    _query_engine: BaseQueryEngine

    def __new__(cls, config: ChocoCocoBrainSettings) -> AgentWorkflow:
        choco_coco_settings = config
        choco_coco_default_behavor = ChocoCocoBrainDefaultBehavor()  # ty: ignore

        ollama_embedding = OllamaEmbedding(
            model_name=choco_coco_settings.embedder.config.model,
            base_url=str(choco_coco_settings.embedder.config.base_url),
        )

        ollama_llm = Ollama(
            base_url=str(choco_coco_settings.llm.config.base_url),
            model=choco_coco_settings.llm.config.model,
            request_timeout=120.0,
        )

        SettingsLLamaIndex.embed_model = ollama_embedding
        SettingsLLamaIndex.llm = ollama_llm

        documents = SimpleDirectoryReader(BASES_DIR).load_data()

        index = VectorStoreIndex.from_documents(
            documents,
            embed_model=SettingsLLamaIndex.embed_model,
        )

        query_engine = index.as_query_engine(
            llm=SettingsLLamaIndex.llm,
            response_mode="compact",
        )

        agent = AgentWorkflow.from_tools_or_functions(
            [cls._search_documents],
            llm=SettingsLLamaIndex.llm,
            output_cls=PokemonAttribute,
            system_prompt=choco_coco_default_behavor.system_prompt,
        )

        cls._query_engine = query_engine

        return agent

    @staticmethod
    async def _search_documents(query: str) -> str:
        response = await ChocoCocoBrain._query_engine.aquery(query)

        return str(response)
