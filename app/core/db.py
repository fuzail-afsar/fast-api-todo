from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session

from app.core import settings


connection_string = str(settings.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string, connect_args={"sslmode": "require"}, pool_recycle=300
)


def init_db(engine=engine) -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


DB = Annotated[Session, Depends(get_session)]
