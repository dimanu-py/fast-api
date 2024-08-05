from fastapi import APIRouter, status, HTTPException, Path

from todo_list.database import Database
from todo_list.models.todos import Todos
from todo_list.router.auth import AuthUser

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all_todos(user: AuthUser, db: Database):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")
    if user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not an admin")

    return db.query(Todos).all()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo_by_id(user: AuthUser, db: Database, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")
    if user.get("role") != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not an admin")

    selected_todo = db.query(Todos).filter_by(id=todo_id).first()

    if selected_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {todo_id} not found")

    db.delete(selected_todo)
    db.commit()
