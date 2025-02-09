# builtin
from os import getenv

# external

from pydantic_settings import BaseSettings, SettingsConfigDict

# internal


class Environment(BaseSettings):
    model_config: SettingsConfigDict = SettingsConfigDict(env_file=".env")
    OPENAI_KEY: str | None = getenv("OPENAI_KEY")
