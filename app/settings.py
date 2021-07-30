from authlib.integrations.starlette_client import OAuth
from pydantic import BaseSettings, Field
from starlette.config import Config


class Settings(BaseSettings):
    env: str = Field("prod", env="ENV")
    app_url: str = Field("http://127.0.0.1:8000/", env="APP_URL")
    db_uri: str = Field(
        "mongodb://localhost:27017", env="DB_URI"
    )

    class Config:
        env_file = '.env'


settings = Settings()

