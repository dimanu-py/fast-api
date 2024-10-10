import datetime

import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from starlette.testclient import TestClient

from todo_list.app import app
from todo_list.models.todos import Todos

TEST_DATABASE = "sqlite:///../testdb.db"

client = TestClient(app)

engine = create_engine(
    TEST_DATABASE,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_test_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_authenticated_user():
    return {"username": "dimanu", "id": 1, "role": "admin"}


@pytest.fixture
def todo_element():
    todo = Todos(
        title="Test Todo",
        description="Test Description",
        owner=1,
        priority=3,
        completed=False,
        due_time=datetime.datetime(2023, 8, 12)
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo

    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()
