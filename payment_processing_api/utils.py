import re
from datetime import datetime, timedelta


def validate_expiration_date(date_str):
    pattern = r"^(0?[1-9]|1[0-2])\/\d{2}$"
    if not re.match(pattern, date_str):
        raise ValueError("Invalid expiration date format (MM/YY)")

    # Convert to datetime object and check for expiry
    expiration_date = datetime.strptime(date_str, "%m/%y")
    today = datetime.today()
    if expiration_date <= today:
        raise ValueError("Card is expired")


def validate_numeric_fields(data):
    for field, value in data.items():
        if field in ("amount", "card_number", "cvv"):
            try:
                float(value)
            except ValueError:
                raise ValueError(f"{field} must be a numeric value")
