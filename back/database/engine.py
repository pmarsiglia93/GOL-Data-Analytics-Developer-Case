from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from database.config.settings import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args=settings.SQLALCHEMY_CONNECT_ARGS
)

session_maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def session_generator() -> Generator[Session, None, None]:
    with session_maker() as session:
        yield session
