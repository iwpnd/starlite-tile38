from typing import Optional

from pydantic import BaseSettings, Field


class Credentials(BaseSettings):
    tile38_uri: Optional[str] = Field(..., env="TILE38_URI")

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = ".env"
        env_file_encoding = "utf-8"
