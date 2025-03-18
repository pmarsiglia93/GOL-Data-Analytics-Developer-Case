from datetime import datetime
from functools import wraps
from typing import Any, Callable, Dict, List

import numpy as np
import pandas as pd

from sqlalchemy import DateTime, Integer, asc, desc, func, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, mapped_column

from database.engine import session_generator

Base = declarative_base()


def session(function: Callable[..., Any]) -> Callable[..., Any]:
    '''
    Provides a session to the decorated function.

    Arguments:
        function (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The decorated function with a session.
    '''

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args[0]._session = next(session_generator())

        try:
            return function(*args, **kwargs)

        finally:
            args[0]._session.close()

    wrapper.__doc__ = function.__doc__
    wrapper.__name__ = function.__name__

    return wrapper


class BaseModel(Base):
    '''
    Base class for SQLAlchemy models with common attributes and methods.
    '''

    __abstract__ = True

    id = mapped_column(Integer, primary_key=True, sort_order=-1)

    created_at = mapped_column(DateTime, default=datetime.utcnow)
    updated_at = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    _session: Session = None

    def __repr__(self) -> str:
        '''
        Return a string representation of the model object.
        '''

        return '<{}(id={}, created_at={}, updated_at={})>'.format(
            self.__class__.__name__,
            self.id,
            self.created_at,
            self.updated_at
        )

    @classmethod
    @session
    def count_all(cls) -> int:
        '''
        Count all objects of this model in the database.

        Returns:
            int: The total number of objects of this model.
        '''

        return cls._session.query(func.count(cls.id)).scalar()

    @classmethod
    @session
    def delete_all(cls) -> None:
        '''
        Delete all objects of this model from the database.

        Returns:
            None
        '''

        cls._session.query(cls).delete()
        cls._session.commit()

    @classmethod
    @session
    def get_all(cls) -> List['BaseModel']:
        '''
        Retrieve all objects of this model from the database.

        Returns:
            List[BaseModel]: A list of all objects of this model.
        '''

        return cls._session.query(cls).all()

    @classmethod
    @session
    def get_dataframe(cls) -> pd.DataFrame:
        '''
        Retrieve all objects of this model as a Pandas DataFrame.

        Returns:
            pd.DataFrame: A Pandas DataFrame containing all objects of this model.
        '''

        return pd.read_sql(cls._session.query(cls).statement, cls._session.get_bind())

    @classmethod
    @session
    def get_id(cls, id: int) -> 'BaseModel':
        '''
        Retrieve an object of this model by its ID.

        Arguments:
            id (int): The ID of the object to retrieve.

        Returns:
            BaseModel: The object with the specified ID.
        '''

        return cls._session.query(cls).filter_by(id=id).first()

    @classmethod
    @session
    def get_limit(cls, limit: int, order_by: Dict[str, str] = {}) -> List['BaseModel']:
        '''
        Retrieve a limited number of objects of this model as a list, ordered by the specified columns.

        Arguments:
            limit (int): The maximum number of objects to retrieve.
            order_by (Dict[str, str]): A dictionary with column names and orders ('asc' or 'desc').

        Returns:
            List[BaseModel]: A list containing a limited number of objects of this model, ordered by the specified columns.
        '''

        order_by = [
            desc(getattr(cls, column))
            if order == 'desc'
            else asc(getattr(cls, column))
            for column, order in order_by.items()
        ]

        return cls._session.query(cls).order_by(*order_by).limit(limit).all()

    @classmethod
    @session
    def save_dataframe(cls, dataframe: pd.DataFrame) -> None:
        '''
        Save all data from a Pandas DataFrame as objects of this model.

        Arguments:
            dataframe (pd.DataFrame): A Pandas DataFrame containing data to be saved.

        Notes:
            This method assumes that the columns in the Pandas DataFrame match the columns of the SQLAlchemy model class.

        Returns:
            None
        '''

        cls._session.bulk_insert_mappings(cls, dataframe.fillna(np.nan).replace(np.nan, None).to_dict(orient='records'))
        cls._session.commit()

    @classmethod
    @session
    def save_dictionary(cls, dictionary: Dict[str, Any]) -> None:
        '''
        Save all data from a dictionary as an object of this model.

        Arguments:
            dictionary (Dict[str, Any]): A dictionary containing data to be saved.

        Notes:
            This method assumes that the items in the dictionary match the columns of the SQLAlchemy model class.

        Returns:
            None
        '''

        cls._session.add(cls(**dictionary))
        cls._session.commit()

    @classmethod
    @session
    def truncate_table(cls) -> None:
        '''
        Truncate the table, deleting all objects and resetting the auto-increment ID field.

        Returns:
            None
        '''

        cls._session.execute(text(f'TRUNCATE TABLE {cls.__tablename__};'))
        cls._session.commit()

    @classmethod
    @session
    def update_id(cls, id: int, data: Dict[str, Any]) -> 'BaseModel':
        '''
        Update an object of this model by its ID with the provided data.

        Arguments:
            id (int): The ID of the object to update.
            data (Dict[str, Any]): A dictionary containing data to be updated.

        Returns:
            BaseModel: The updated object with the specified ID.
        '''

        obj = cls._session.query(cls).filter_by(id=id).first()

        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        cls._session.commit()

        obj = cls._session.query(cls).filter_by(id=id).first()

        return obj

    @classmethod
    @session
    def upsert_dataframe(cls, dataframe: pd.DataFrame, keys: list[str]) -> None:
        '''
        Upsert objects of this model by given keys with the provided Pandas DataFrame.

        Arguments:
            dataframe (pd.DataFrame): A Pandas DataFrame containing data to be upserted.
            keys (list[str]): The keys of the objects to upsert.

        Returns:
            None
        '''

        for data in dataframe.fillna(np.nan).replace(np.nan, None).to_dict(orient='records'):
            obj = cls._session.query(cls).filter_by(**{key: data[key] for key in keys}).first()

            if obj:
                for key, value in data.items():
                    setattr(obj, key, value)
            else:
                cls._session.add(cls(**data))

        cls._session.commit()
