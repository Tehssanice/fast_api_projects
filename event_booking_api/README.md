# Event Booking API Documentation

## Overview

This document outlines the FastAPI endpoint for booking events, such as concerts and workshops.

### Features

- Use request body parameters for attendee information (name, email, age), event details (name, date, location), and ticket type.
- Implement string validation for attendee details and event name.
- Apply numeric validation for attendee age.
- Validate ticket type against available options.
- Return booking confirmation with event details.

## Endpoint Details

### Route: /events/book

- **Method**: POST
- **Description**: Book an event ticket.
- **Request Body**:
  - attendee_name: string (required)
  - attendee_email: string (required, valid email format)
  - attendee_age: integer (required, positive value)
  - event_name: string (required)
  - event_date: string (required, format: YYYY-MM-DD)
  - event_location: string (required)
  - ticket_type: string (required, valid options: general, VIP)
- **Response**:
  - Success: 200 OK with booking confirmation
  - Error: 400 Bad Request

### Validation

- Attendee name and event name must be strings.
- Attendee age must be a positive integer.
- Ticket type must be either "general" or "VIP".

## Testing

The API has been thoroughly tested with various scenarios, including full and partial bookings, to ensure proper functionality and error handling.
