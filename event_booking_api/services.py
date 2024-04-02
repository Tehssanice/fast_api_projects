async def event_processing(event_booking):
    """
     Process the booking details, this is for the business logic
     """

    event_info = {

        "client_name": event_booking.attendee_info.name,
        "client_age": event_booking.attendee_info.age,
        "client_email": event_booking.attendee_info.email,
        "event_theme": event_booking.event_details.theme,
        "event_date": event_booking.event_details.date.strftime("%Y-%m-%d")

    }

    return event_info
