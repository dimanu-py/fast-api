from fastapi import status

from tests.conftest import client, engine, get_test_db, get_test_authenticated_user, todo_element, TestingSessionLocal
from todo_list import database
from todo_list.app import app
from todo_list.models.todos import Todos
from todo_list.router import auth

database.Base.metadata.create_all(bind=engine)

app.dependency_overrides[database.get_database] = get_test_db
app.dependency_overrides[auth.get_authenticated_user] = get_test_authenticated_user


class TestAdmin:

    def test_admin_can_read_all_users_tasks(self, todo_element):
        response = client.get("/admin/todo")

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

    def test_admin_can_delete_any_user_task_with_id(self, todo_element):
        response = client.delete("/admin/todo/1")

        assert response.status_code == status.HTTP_204_NO_CONTENT

        db = TestingSessionLocal()
        task_amount = db.query(Todos).count()
        db.close()
        assert task_amount == 0

    def test_raises_error_when_task_to_delete_is_not_found(self):
        response = client.delete("/admin/todo/2")

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json() == {"detail": "Todo with id 2 not found"}
