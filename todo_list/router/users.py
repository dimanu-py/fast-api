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
        phone_number=user.phone_number
    )

    db.add(new_user)
    db.commit()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_logged_user(user: AuthUser, db: Database) -> None:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")
    return db.query(Users).filter_by(id=user.get("id")).first()


@router.put("/password/{password}", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: AuthUser, password: str, db: Database) -> None:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")

    user = db.query(Users).filter_by(id=user.get("id")).first()
    user.hashed_password = hash_password(password)
    db.add(user)
    db.commit()


@router.put("/phone_number/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(user: AuthUser, phone_number: str, db: Database) -> None:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User authentication failed")

    user = db.query(Users).filter_by(id=user.get("id")).first()
    user.phone_number = phone_number
    db.add(user)
    db.commit()
