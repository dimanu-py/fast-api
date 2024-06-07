from typing import Generator, Annotated, Type

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

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


@app.get("/todo")
async def read_all_todos(db: Session = Depends(get_database)):
    return db.query(models.Todos).all()