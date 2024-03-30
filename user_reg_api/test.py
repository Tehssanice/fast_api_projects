from fastapi.testclient import TestClient
from main import app
from models import UserRegistration

client = TestClient(app)


def test_register_user():
    test_user_data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "StrongPassword123!"
    }

    # Send a POST request to the registration endpoint
    response = client.post("/register/", json=test_user_data)

    assert response.status_code == 200
    assert response.json() == test_user_data
