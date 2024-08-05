from datetime import timedelta, datetime, timezone

import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status

from todo_list.database import get_database
from todo_list.models.users import Users
from todo_list.schemas.users import Token

router = APIRouter(prefix="/auth", tags=["Auth"])

EXPIRE_TIME = 20
SECRET_KEY = "29bb1a587cfccb051b271484e593e08eda02c1b470c767a424fcbe5cee5a4186"
ALGORITHM = "HS256"

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/login")


def create_access_token(username: str, user_id: int, expires_delta: timedelta) -> str:
    payload = {
        "sub": username,
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + expires_delta
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def get_authenticated_user(token: str = Depends(oauth2_bearer)) -> dict[str, str | int]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("user_id")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return {"username": username, "id": user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


@router.post("/login", status_code=status.HTTP_200_OK, response_model=Token)
async def login_for_access_token(form_data=Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_database)):
    user = db.query(Users).filter(Users.username == form_data.username).first()

    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {form_data.username} not found")
    if not bcrypt.checkpw(form_data.password.encode("utf-8"), user.hashed_password.encode("utf-8")):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password")

    access_token = create_access_token(user.username, user.id, timedelta(minutes=EXPIRE_TIME))

    return {"access_token": access_token, "token_type": "bearer"}
