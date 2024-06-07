from typing import Generator

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

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


@app.get("/todo", status_code=status.HTTP_200_OK)
async def read_all_todos(db: Session = Depends(get_database)):
    return db.query(models.Todos).all()


@app.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_database)):
    selected_todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if selected_todo is not None:
        return selected_todo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo not with id {todo_id} not found")
