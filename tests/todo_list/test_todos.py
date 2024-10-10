from fastapi import status

from tests.conftest import client, engine, get_test_db, get_test_authenticated_user, TestingSessionLocal
from tests.conftest import todo_element
from todo_list import database
from todo_list.app import app
from todo_list.models.todos import Todos
from todo_list.router import auth

database.Base.metadata.create_all(bind=engine)

app.dependency_overrides[database.get_database] = get_test_db
app.dependency_overrides[auth.get_authenticated_user] = get_test_authenticated_user


class TestTodo:

    def test_return_empty_list_when_there_are_no_tasks(self):
        response = client.get("/todo/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_get_all_tasks_for_user(self, todo_element):
        response = client.get("/todo/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [{
            "id": 1,
            "title": "Test Todo",
            "description": "Test Description",
            "priority": 3,
            "completed": False,
            "owner": 1,
            "due_time": "2023-08-12T00:00:00"
        }]

    def test_get_one_task_by_id(self, todo_element):
        response = client.get("/todo/1")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "id": 1,
            "title": "Test Todo",
            "description": "Test Description",
            "priority": 3,
            "completed": False,
            "owner": 1,
            "due_time": "2023-08-12T00:00:00"
        }

    def test_raises_error_when_task_do_not_exist(self, todo_element):
        response = client.get("/todo/2")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Todo with id 2 not found"}

    def test_user_can_create_a_task(self, todo_element):
        request = {
            "title": "New Todo",
            "description": "New Description",
            "priority": 1,
            "completed": False,
            "due_time": "2023-08-12T00:00:00"
        }

        response = client.post("/todo/", json=request)

        assert response.status_code == status.HTTP_201_CREATED

        db = TestingSessionLocal()
        tasks_amount = len(db.query(Todos).all())
        assert tasks_amount == 2

    def test_user_can_complete_a_task(self, todo_element):
        request = {
            "id": 1,
            "title": "Test Todo",
            "description": "Test Description",
            "priority": 3,
            "completed": True,
            "owner": 1,
            "due_time": "2023-08-12T00:00:00"
        }

        response = client.put("/todo/1", json=request)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        db = TestingSessionLocal()
        updated_todo = db.query(Todos).filter_by(id=1).first()
        assert updated_todo.completed is True

    def test_user_can_update_any_task_field_by_id(self, todo_element):
        request = {
            "id": 1,
            "title": "Updated Todo",
            "description": "Updated Description",
            "priority": 1,
            "completed": False,
            "owner": 1,
            "due_time": "2023-08-12T00:00:00"
        }

        response = client.put("/todo/1", json=request)

        assert response.status_code == status.HTTP_204_NO_CONTENT

        db = TestingSessionLocal()
        updated_todo = db.query(Todos).filter_by(id=1).first()
        assert updated_todo.description == "Updated Description"

    def test_raises_error_when_task_to_be_updated_do_not_exist(self):
        request = {
            "id": 2,
            "title": "Updated Todo",
            "description": "Updated Description",
            "priority": 1,
            "completed": False,
            "owner": 1,
            "due_time": "2023-08-12T00:00:00"
        }

        response = client.put("/todo/2", json=request)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Todo with id 2 not found"}

    def test_user_can_delete_a_task_by_id(self, todo_element):
        response = client.delete("/todo/1")

        assert response.status_code == status.HTTP_204_NO_CONTENT

        db = TestingSessionLocal()
        tasks_amount = len(db.query(Todos).all())
        assert tasks_amount == 0

    def test_raises_error_if_task_to_be_deleted_do_not_exist(self):
        response = client.delete("/todo/2")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Todo with id 2 not found"}