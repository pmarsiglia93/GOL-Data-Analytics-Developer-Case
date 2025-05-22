import json
import os
import secrets
from pathlib import Path
from typing import Any, List, Union
from pydantic import validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Carrega o arquivo .env
load_dotenv()


class Settings(BaseSettings):
    PROJECT_BASE: str = str(Path(__file__).parent.parent)

    PROJECT_NAME: str = 'GDADC'

    API_V1_STR: str = '/api/v1'

    # Agora com fallback para 'DEV'
    ENV: Union[str, None] = os.getenv('ENV', 'DEV')

    SECRET_KEY: str = secrets.token_urlsafe(32)

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:8000"]'
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, value: Union[str, List[str]]) -> List[str]:
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return [item.strip() for item in value.split(',')]
        elif isinstance(value, list):
            return value

        raise ValueError(value)

    # Authentication
    AUTH_TOKEN_IV: str = '1234567800000737'
    AUTH_TOKEN_KEY: str = 'G3PZaJVsQv03LjLKghCHUq9yiJt6sYVpdVlPOseHWB4='
    AUTH_TOKEN_PASS: str = 'AezTlUiFWgi4A2G3wchbLuQSUF90njnGcxDsppQBqJkRo'

    class Config:
        case_sensitive = True


settings = Settings()
