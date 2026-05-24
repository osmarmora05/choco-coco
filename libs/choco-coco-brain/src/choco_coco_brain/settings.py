from pydantic import BaseModel, AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings import YamlConfigSettingsSource
from pathlib import Path


LIB_DIR = Path(__file__).resolve().parent.parent.parent
YAML_PATH = LIB_DIR / "brain_config.yaml"


class ChocoCocoBrainLLMSubConfig(BaseModel):
    model: str
    base_url: AnyHttpUrl


class ChocoCocoBrainEmbedderSubConfig(BaseModel):
    model: str
    base_url: AnyHttpUrl


class ChocoCocoBrainLLMConfig(BaseModel):
    config: ChocoCocoBrainLLMSubConfig


class ChocoCocoBrainEmbedderConfig(BaseModel):
    config: ChocoCocoBrainEmbedderSubConfig


class ChocoCocoBrainSettings(BaseSettings):
    llm: ChocoCocoBrainLLMConfig
    embedder: ChocoCocoBrainEmbedderConfig


class ChocoCocoBrainDefaultBehavor(BaseSettings):
    system_prompt: str

    model_config = SettingsConfigDict(yaml_file=YAML_PATH)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls,
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        return (YamlConfigSettingsSource(settings_cls),)
