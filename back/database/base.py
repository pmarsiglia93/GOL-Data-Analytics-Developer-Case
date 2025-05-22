from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict, List

import numpy as np
import pandas as pd

from sqlalchemy import DateTime, Integer, asc, desc, func, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, mapped_column

from database.engine import session_generator

# Definição da base
Base = declarative_base()

# Definição do decorador `session`
def session(function: Callable[..., Any]) -> Callable[..., Any]:
    '''
    Provides a session to the decorated function.
    '''

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args[0]._session = next(session_generator())

        try:
            return function(*args, **kwargs)

        finally:
            args[0]._session.close()

    return wrapper


class BaseModel(Base):
    '''
    Base class for SQLAlchemy models with common attributes and methods.
    '''

    __abstract__ = True

    id = mapped_column(Integer, primary_key=True)
    created_at = mapped_column(DateTime, default=datetime.utcnow)
    updated_at = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    _session: Session = None

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id}, created_at={self.created_at}, updated_at={self.updated_at})>"

    @classmethod
    @session
    def count_all(cls) -> int:
        return cls._session.query(func.count(cls.id)).scalar()

    @classmethod
    @session
    def delete_all(cls) -> None:
        cls._session.query(cls).delete()
        cls._session.commit()

    @classmethod
    @session
    def get_all(cls) -> List['BaseModel']:
        return cls._session.query(cls).all()

    @classmethod
    @session
    def get_dataframe(cls) -> pd.DataFrame:
        return pd.read_sql(cls._session.query(cls).statement, cls._session.get_bind())

    @classmethod
    @session
    def get_id(cls, id: int) -> 'BaseModel':
        return cls._session.query(cls).filter_by(id=id).first()

    @classmethod
    @session
    def get_limit(cls, limit: int, order_by: Dict[str, str] = {}) -> List['BaseModel']:
        order_by = [
            desc(getattr(cls, column)) if order == 'desc' else asc(getattr(cls, column))
            for column, order in order_by.items()
        ]
        return cls._session.query(cls).order_by(*order_by).limit(limit).all()

    @classmethod
    @session
    def save_dataframe(cls, dataframe: pd.DataFrame) -> None:
        cls._session.bulk_insert_mappings(cls, dataframe.fillna(np.nan).replace(np.nan, None).to_dict(orient='records'))
        cls._session.commit()

    @classmethod
    @session
    def save_dictionary(cls, dictionary: Dict[str, Any]) -> None:
        cls._session.add(cls(**dictionary))
        cls._session.commit()

    @classmethod
    @session
    def truncate_table(cls) -> None:
        cls._session.execute(text(f"TRUNCATE TABLE {cls.__tablename__}"))
        cls._session.commit()

    @classmethod
    @session
    def update_id(cls, id: int, data: Dict[str, Any]) -> 'BaseModel':
        obj = cls._session.query(cls).filter_by(id=id).first()
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        cls._session.commit()
        return obj

    @classmethod
    @session
    def upsert_dataframe(cls, dataframe: pd.DataFrame, keys: list[str]) -> None:
        for data in dataframe.fillna(np.nan).replace(np.nan, None).to_dict(orient='records'):
            obj = cls._session.query(cls).filter_by(**{key: data[key] for key in keys}).first()
            if obj:
                for key, value in data.items():
                    setattr(obj, key, value)
            else:
                cls._session.add(cls(**data))
        cls._session.commit()
