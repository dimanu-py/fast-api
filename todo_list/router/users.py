import bcrypt
from fastapi import APIRouter, status, HTTPException

from todo_list.database import Database
from todo_list.models.users import Users
from todo_list.router.auth import AuthUser
from todo_list.schemas.users import UserRequest

router = APIRouter(prefix="/user", tags=["Users"])


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, db: Database) -> None:
    new_user = Users(
        role=user.role,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
