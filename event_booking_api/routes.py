from fastapi import APIRouter, HTTPException
from services import book_event
from models import BookingRequest

router = APIRouter()


@router.post("/book-event/")
async def book_event_endpoint(booking_request: BookingRequest):
    try:
        return book_event(booking_request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
