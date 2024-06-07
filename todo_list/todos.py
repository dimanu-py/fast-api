from typing import Generator

from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

from todo_list import models
from todo_list.database import engine, SessionLocal
from todo_list.schemas import TodoRequest

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
async def get_todo_by_id(todo_id: int = Path(gt=0), db: Session = Depends(get_database)):
    selected_todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    if selected_todo is not None:
        return selected_todo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo not with id {todo_id} not found")


@app.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoRequest, db: Session = Depends(get_database)) -> None:
    new_todo = models.Todos(**todo.dict())

    db.add(new_todo)
    db.commit()


@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo: TodoRequest, todo_id: int = Path(gt=0), db: Session = Depends(get_database)) -> None:
    selected_todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if selected_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")

    selected_todo.title = todo.title
    selected_todo.description = todo.description
    selected_todo.priority = todo.priority
    selected_todo.completed = todo.completed

    db.add(selected_todo)
    db.commit()


@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int = Path(gt=0), db: Session = Depends(get_database)) -> None:
    selected_todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()

    if selected_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")

    db.delete(selected_todo)
    db.commit()
