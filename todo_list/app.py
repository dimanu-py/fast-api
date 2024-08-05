from fastapi import FastAPI

from todo_list import database
from todo_list.router import users, todos, auth, admin

app = FastAPI()

database.Base.metadata.create_all(bind=database.engine)

app.include_router(users.router)
app.include_router(todos.router)
app.include_router(auth.router)
app.include_router(admin.router)
