from typing import Generator

from fastapi import FastAPI
from todo_list import models
from todo_list.database import engine, Session

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_database() -> Generator[Session]:
    db = Session()
    try:
        yield db
    finally:
        db.close()