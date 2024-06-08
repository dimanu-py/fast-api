from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from todo_list.database import get_database
from todo_list.models.users import Users
from todo_list.schemas.users import UserRequest

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, db: Session = Depends(get_database)) -> None:
    new_user = Users(**user.model_dump())

    db.add(new_user)
    db.commit()
