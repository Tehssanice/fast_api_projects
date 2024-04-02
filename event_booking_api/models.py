from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum


class AttendeeInfo(BaseModel):
    name: str = Field(min_length=3, max_length=20, description="Name of the Attendee", examples=[
                      "Mark Thundry"], title="Name", pattern="^[a-zA-Z ]+$")
    email: EmailStr
    age: int = Field(gt=0, lt=90, description="Age of the passenger", examples=[
                     25], title="Age")


class EventDetails(BaseModel):
    theme: str = Field(description="The event theme",
                       examples=["Joy of Coding"])
    date: datetime
    location: str = Field(min_length=3, max_length=20, description="Location of the event", examples=[
                          "HillView Event Center"], title="Location", pattern="^[a-zA-Z ]+$")


class TicketTypeEnum(str, Enum):
    VIP = "VIP"
    STANDARD = "STANDARD"


class TicketType(BaseModel):
    ticket_type: TicketTypeEnum


class BookingEvent(BaseModel):
    attendee_info: AttendeeInfo
    event_details: EventDetails
    ticket_typee: TicketType
