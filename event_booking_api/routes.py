
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from services import event_processing
from models import BookingEvent

router = APIRouter(prefix="/events")


@router.post("/")
async def book_event(event_booking: BookingEvent):
    event_info = await event_processing(event_booking)
    return JSONResponse(status_code=200, content={"data": event_info, "message": "Event booked"})
