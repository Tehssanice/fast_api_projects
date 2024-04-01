from pydantic import BaseModel


class PaymentRequest(BaseModel):
    amount: float
    card_number: str
    expiration_date: str
    cvv: str
