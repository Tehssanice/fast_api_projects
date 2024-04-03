from fastapi.testclient import TestClient
from main import app
from models import UserRegistration

client = TestClient(app)


def test_register_user():
    test_user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "StrongPassword12@!"
    }

    # Send a POST request to the registration endpoint
    response = client.post("user/register/", json=test_user_data)

    assert response.status_code == 200
    assert response.json() == test_user_data
