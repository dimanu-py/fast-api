from fastapi import FastAPI

from todo_list import database
from todo_list.database import engine
from todo_list.router import users, todos, auth

app = FastAPI()

database.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(todos.router)
app.include_router(auth.router)
