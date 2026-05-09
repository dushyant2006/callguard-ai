import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    KAFKA_BROKER_URL: str = "localhost:9092"
    OPENAI_API_KEY: str = "mock-key"
    USE_MOCK_AI: bool = True
    
    # DB for pgvector
    POSTGRES_USER: str = "callguard"
    POSTGRES_PASSWORD: str = "securepassword"
    POSTGRES_DB: str = "callguard_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
