from fastapi import FastAPI
from todo_list import models
from todo_list.database import engine


app = FastAPI()


models.Base.metadata.create_all(bind=engine)