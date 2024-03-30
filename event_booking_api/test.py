from fastapi.testclient import TestClient
from main import app
from models import TicketType

client = TestClient(app)


def test_book_event():
    test_booking_request = {
        "attendee": {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": 30
        },
        "event_details": {
            "name": "Concert",
            "date": "2024-02-15",
            "location": "City Concert Hall"
        },
        "ticket_type": TicketType.VIP
    }

    response = client.post("/book-event/", json=test_booking_request)
    assert response.status_code == 200
