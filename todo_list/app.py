from fastapi import FastAPI

from todo_list import models
from todo_list.database import engine
from todo_list.routers import auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
