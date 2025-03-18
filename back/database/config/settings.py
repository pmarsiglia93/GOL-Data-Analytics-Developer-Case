import json
import os

from typing import Any

from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'GDADC'

    DB_ENGINE: str | None = os.getenv('DB_ENGINE')
    DB_HOST: str | None = os.getenv('DB_HOST')
    DB_PORT: str | None = os.getenv('DB_PORT')
    DB_NAME: str | None = os.getenv('DB_NAME')
    DB_USER: str | None = os.getenv('DB_USER')
    DB_PASSWORD: str | None = os.getenv('DB_PASSWORD')
    DB_DRIVER: str | None = os.getenv('DB_DRIVER')

    SQLALCHEMY_CONNECT_ARGS: dict | None = json.loads(os.getenv('SQLALCHEMY_CONNECT_ARGS', '{}'))
    SQLALCHEMY_DATABASE_URI: str | None = os.getenv('SQLALCHEMY_DATABASE_URI')

    DATABASE_TABLENAME_BASE: str | None = os.getenv('DATABASE_TABLENAME_BASE', f'{PROJECT_NAME.lower()}_')

    @validator('SQLALCHEMY_DATABASE_URI', pre=True)
    def assemble_db_uri(
        cls,
        value: str | None,
        values: dict[str, Any]
    ) -> Any:
        if isinstance(value, str):
            return value

        elif all([
            values['DB_ENGINE'],
            values['DB_USER'],
            values['DB_PASSWORD'],
            values['DB_HOST'],
            values['DB_PORT'],
            values['DB_NAME'],
            values['DB_DRIVER'],
        ]):
            return '{}://{}:{}@{}:{}/{}?driver={}'.format(
                values['DB_ENGINE'],
                values['DB_USER'],
                values['DB_PASSWORD'],
                values['DB_HOST'],
                values['DB_PORT'],
                values['DB_NAME'],
                values['DB_DRIVER']
            )

        SQLALCHEMY_CONNECT_ARGS = {
            'check_same_thread': False
        }

        return 'sqlite:///db.sqlite3'

    class Config:
        case_sensitive = True


settings = Settings()
