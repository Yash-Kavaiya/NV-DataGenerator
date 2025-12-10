import os
from pathlib import Path
from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    nvidia_api_key: str = Field(default="")
    artifact_path: Path = Field(default=Path("./artifacts"))


@lru_cache
def get_settings() -> Settings:
    return Settings()
