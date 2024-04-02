from fastapi.testclient import TestClient
from main import app
from models import TicketType


client = TestClient(app)


def test_book_event():
    test_booking_request = {
        "attendee_info": {
            "name": "Mark Doe",
            "email": "john.doe@example.com",
            "age": 30
        },
        "event_details": {
            "theme": "Concert",
            "date": "2024-02-15",
            "location": "City Concert Hall"
        },
        # Invalid ticket type for testing error case
        "ticket_type": "INVALID_TICKET_TYPE"
    }
    response = client.post("/events/", json=test_booking_request)
    assert response.status_code == 422  # Expecting a bad request status code
