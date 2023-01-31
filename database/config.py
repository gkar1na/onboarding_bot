# coding: utf-8

from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_PATH: Optional[str]

    class Config:
        env_prefix = ''
        # uncomment when testing locally
        env_file = '../.env'
        env_file_encoding = 'utf-8'


settings = Settings()
