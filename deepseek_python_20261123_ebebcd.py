import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    upstream_url: str = os.getenv("UPSTREAM_URL", "https://api.groq.com/openai/v1")
    upstream_api_key: str = os.getenv("UPSTREAM_API_KEY", "")
    app_api_keys: str = os.getenv("APP_API_KEYS", "")

    # What the client sees
    model_alias: str = os.getenv("MODEL_ALIAS", "oceaneyez")

    # What the upstream actually runs
    model_name: str = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

    request_timeout: float = float(os.getenv("REQUEST_TIMEOUT", "120.0"))

    @property
    def valid_keys(self) -> set[str]:
        return {k.strip() for k in self.app_api_keys.split(",") if k.strip()}


settings = Settings()