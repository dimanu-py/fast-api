from typing import Generator, Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///todo_list/todos_application.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Database = Annotated[Session, Depends(get_database)]
