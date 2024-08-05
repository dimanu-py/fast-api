from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from starlette import status

from todo_list.database import get_database
from todo_list.models.todos import Todos
from todo_list.router.users import get_authenticated_user
from todo_list.schemas.todos import TodoRequest

router = APIRouter(prefix="/todo", tags=["Todos"])


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all_todos(db: Session = Depends(get_database)):
    return db.query(Todos).all()


@router.get("/{todo_id}", status_code=status.HTTP_200_OK)
async def get_todo_by_id(todo_id: int = Path(gt=0), db: Session = Depends(get_database)):
    selected_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if selected_todo is not None:
        return selected_todo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo not with id {todo_id} not found")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoRequest, db: Session = Depends(get_database),
                      user: dict[str, str] = Depends(get_authenticated_user)) -> None:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")

    new_todo = Todos(**todo.dict(), owner=user.get("id"))

    db.add(new_todo)
    db.commit()


@router.put("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo: TodoRequest, todo_id: int = Path(gt=0), db: Session = Depends(get_database)) -> None:
    selected_todo = db.query(Todos).filter(Todos.id == todo_id).first()

    if selected_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")

    selected_todo.title = todo.title
    selected_todo.description = todo.description
    selected_todo.priority = todo.priority
    selected_todo.completed = todo.completed

    db.add(selected_todo)
    db.commit()


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int = Path(gt=0), db: Session = Depends(get_database)) -> None:
    selected_todo = db.query(Todos).filter(Todos.id == todo_id).first()

    if selected_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")

    db.delete(selected_todo)
    db.commit()
