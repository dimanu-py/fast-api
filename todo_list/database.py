from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///todo_list/todos.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
