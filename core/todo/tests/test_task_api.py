from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user_obj = User.objects.create(username="mopiry", password="a/@1234567",)
    return user_obj


@pytest.mark.django_db
class TestTaskApi:
    def test_get_task_response_200_status(self, api_client):
        url = reverse("todo:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_task_response_200_status(self, api_client):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "test",
            "description": "desc",
            "completed": False,
        
        }
        response = api_client.post(url, data)
        assert response.status_code == 200

    def test_create_task_response_201_status(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {
            "title": "test",
            "description": "desc",
            "completed": False,
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_task_invalid_data_response_400_status(self, api_client, common_user):
        url = reverse("todo:api-v1:task-list")
        data = {"description": "test",}
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400



