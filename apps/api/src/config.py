from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8080, alias="API_PORT")

    ollama_base_url: AnyHttpUrl = Field(
        AnyHttpUrl("http://ollama:11434"), alias="OLLAMA_BASE_URL"
    )

    embedder_base_url: AnyHttpUrl = Field(
        AnyHttpUrl("http://ollama:11434"), alias="EMBEDDER_BASE_URL"
    )

    ollama_llm_model: str = Field(
        default="qwen2.5:3b-instruct", alias="OLLAMA_LLM_MODEL"
    )

    embedder_model: str = Field(default="embeddinggemma:300m", alias="EMBEDDER_MODEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


app_config = AppConfig()
