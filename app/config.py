from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    project_id: str | None = None
    subscription_id: str | None = None
    apollo_router_url: str | None = None
    shopify_api_version: str = "2025-10"


settings = Settings()