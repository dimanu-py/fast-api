from datetime import timedelta, datetime, timezone

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session

from todo_list.database import get_database
from todo_list.models.users import Users
from todo_list.schemas.users import UserRequest, Token

EXPIRE_TIME = 20

router = APIRouter(prefix="/user", tags=["Users"])

SECRET_KEY = "29bb1a587cfccb051b271484e593e08eda02c1b470c767a424fcbe5cee5a4186"
ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def create_access_token(username: str, user_id: int, expires_delta: timedelta) -> str:
    payload = {
        "sub": username,
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + expires_delta
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserRequest, db: Session = Depends(get_database)) -> None:
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


@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
async def login_for_access_token(form_data=Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_database)):
    user = db.query(Users).filter(Users.username == form_data.username).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {form_data.username} not found")
    if not bcrypt.checkpw(form_data.password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    access_token = create_access_token(user.username, user.id, timedelta(minutes=EXPIRE_TIME))

    return {"access_token": access_token, "token_type": "bearer"}
