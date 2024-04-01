import requests

# Example of valid payment data
valid_data = {
    "amount": 100.50,
    # Placeholder for test card number
    "card_number": "1234567890123456",
    "expiration_date": "05/25",
    "cvv": "123"
}

# Example invalid payment data (different variations for testing)
invalid_data_list = [
    # Non-numeric amount
    {"amount": "invalid amount", "card_number": "1234567890123456",
        "expiration_date": "05/25", "cvv": "123"},

    {"amount": 100.50, "card_number": "invalid_card_number",
        "expiration_date": "05/25", "cvv": "123"},

    {"amount": 100.50, "card_number": "1234567890123456",
        "expiration_date": "invalid_format", "cvv": "123"},

    {"amount": 100.50, "card_number": "1234567890123456",
        "expiration_date": "12/23", "cvv": "123"},

    # Missing field
    {"amount": 100.50, "card_number": "1234567890123456", "expiration_date": "05/25"},
]


def test_payment_processing():

    base_url = "http://localhost:8000/api/payments"

    # Valid payment data
    response = requests.post(base_url, json=valid_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Payment processing initiated"}

    # Invalid data set
    for invalid_data in invalid_data_list:
        response = requests.post(base_url, json=invalid_data)
        assert response.status_code == 422


if __name__ == "__main__":
    test_payment_processing()
