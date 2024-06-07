from typing import Generator

from fastapi import FastAPI
from todo_list import models
from todo_list.database import engine, SessionLocal

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_database() -> Generator[SessionLocal, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()