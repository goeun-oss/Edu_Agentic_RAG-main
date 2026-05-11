from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")
    openai_api_key: str = Field("", alias="OPENAI_API_KEY")
    llm_model: str = Field("gpt-4.1-mini", alias="LLM_MODEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()

