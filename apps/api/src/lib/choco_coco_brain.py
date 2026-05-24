from choco_coco_brain import (
    ChocoCocoBrain,
    ChocoCocoBrainEmbedderConfig,
    ChocoCocoBrainEmbedderSubConfig,
    ChocoCocoBrainLLMConfig,
    ChocoCocoBrainLLMSubConfig,
    ChocoCocoBrainSettings,
)

from config import app_config


def get_coquito():  # noqa: ANN201 bruh, suck types
    coquito = ChocoCocoBrain(
        ChocoCocoBrainSettings(
            llm=ChocoCocoBrainLLMConfig(
                config=ChocoCocoBrainLLMSubConfig(
                    model=app_config.ollama_llm_model,
                    base_url=app_config.ollama_base_url,
                ),
            ),
            embedder=ChocoCocoBrainEmbedderConfig(
                config=ChocoCocoBrainEmbedderSubConfig(
                    model=app_config.embedder_model,
                    base_url=app_config.embedder_base_url,
                ),
            ),
        )
    )

    return coquito
