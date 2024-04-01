from fastapi import APIRouter, Body, HTTPException

from models import PaymentRequest
from utils import validate_expiration_date, validate_numeric_fields

app = APIRouter()


@app.post("/payments")
async def process_payment(payment_data: PaymentRequest = Body(...)):
    # Validate numeric fields
    validate_numeric_fields(payment_data.dict())

    # Validate expiration date format and expiry
    validate_expiration_date(payment_data.expiration_date)

    print(f"Processing payment for amount: {payment_data.amount}")
    return {"message": "Payment processing initiated"}
