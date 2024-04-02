from fastapi.testclient import TestClient
from main import api

client = TestClient(api)


def test_payment_processing():
    response = client.post(
        "/api/payments/",
        json={
            "amount": 100.50,
            "card_number": "1234567890123456",
            "expiration_date": "05/25",
            "cvv": "123"
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Payment processing initiated"
    }
