from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    test_login: str = Field(default="")
    test_user: str = Field(default="")
    test_token: str = Field(default="")
    test_password: str = Field(default="")
    back_end_url: str = Field(default="")
    front_end_url: str = Field(default="")
    storage_state_path: str = Field(default="")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="forbid",      # запретить лишние поля
        env_prefix=""        # если переменные без префикса
    )