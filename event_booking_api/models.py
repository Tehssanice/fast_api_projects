from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


class Attendee(BaseModel):
    name: str
    email: EmailStr
    age: int


class EventDetails(BaseModel):
    name: str
    date: str
    location: str


class TicketType(str):
    VIP = "VIP"
    STANDARD = "STANDARD"


class BookingRequest(BaseModel):
    attendee: Attendee
    event_details: EventDetails
    ticket_type: TicketType


class BookingDB(BaseModel):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String)
    event_date = Column(DateTime)
    event_location = Column(String)
    attendee_name = Column(String)
    attendee_email = Column(String)
    attendee_age = Column(Integer)
    ticket_type = Column(String)
