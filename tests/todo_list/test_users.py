from fastapi import status

from tests.conftest import client, engine, get_test_db, get_test_authenticated_user, todo_element, TestingSessionLocal
from todo_list import database
from todo_list.app import app
from todo_list.models.todos import Todos
from todo_list.router import auth
from todo_list.schemas.users import UserRequest

database.Base.metadata.create_all(bind=engine)

app.dependency_overrides[database.get_database] = get_test_db
app.dependency_overrides[auth.get_authenticated_user] = get_test_authenticated_user


class TestUsers:

    def test_not_logged_user_can_create_new_user(self):
        request = UserRequest(
            username="johndoe",
            password="password",
            role="user",
            email="user@gmail.com",
            first_name="John",
            last_name="Doe",
            phone_number="123456789"
        )

        response = client.post("/users/", json=request)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {"username": "new_user", "id": 1, "role": "user"}