import json
import os
import secrets

from pathlib import Path
from typing import Any

from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_BASE: str = str(Path(__file__).parent.parent)

    PROJECT_NAME: str = 'GDADC'

    API_V1_STR: str = '/api/v1'

    ENV: str | None = os.getenv('ENV')

    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: ['http://localhost', 'http://localhost:8000']
    BACKEND_CORS_ORIGINS: list[str] = ['*']

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, value: str | list[str]) -> list[str] | str:
        if isinstance(value, str) and not value.startswith('['):
            return [item.stritemp() for item in value.split(',')]
        elif isinstance(value, list | str):
            return value

        raise ValueError(value)

    # Authentication
    # 32ELwKq5ATgDn5YSyDd93pKzIkM4KJj//ZPsbEeqjq+0SWFFdX1K7szFRNqZi25G

    AUTH_TOKEN_IV: str = '1234567800000737'
    AUTH_TOKEN_KEY: str = 'G3PZaJVsQv03LjLKghCHUq9yiJt6sYVpdVlPOseHWB4='
    AUTH_TOKEN_PASS: str = 'AezTlUiFWgi4A2G3wchbLuQSUF90njnGcxDsppQBqJkRo'

    class Config:
        case_sensitive = True


settings = Settings()
