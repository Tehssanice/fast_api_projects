# Flight Booking API Documentation

## Overview

This document outlines the FastAPI route for booking flights.

### Features

- Utilize request body parameters for passenger information (name, age, contact details), flight details (origin, destination, date), and seat preferences.
- Implement string validation for passenger names and contact details.
- Apply numeric validation for passenger age and flight-related fields.
- Ensure seat preferences are within valid options.
- Simulate flight booking process and return booking confirmation.
- Test the API with different combinations of inputs.

## Endpoint Details

### Route: /flights/book

- **Method**: POST
- **Description**: Book a flight ticket.
- **Request Body**:
  - passenger_name: string (required)
  - passenger_age: integer (required, positive value)
  - passenger_contact: string (required, valid contact details)
  - flight_origin: string (required)
  - flight_destination: string (required)
  - flight_date: string (required, format: YYYY-MM-DD)
  - seat_preference: string (required, valid options: window, aisle, middle)
- **Response**:
  - Success: 200 OK with booking confirmation
  - Error: 400 Bad Request

### Validation

- Passenger name and contact details must be strings.
- Passenger age must be a positive integer.
- Flight origin and destination must be strings.
- Flight date must be in the format YYYY-MM-DD.
- Seat preference must be one of the following: "window", "aisle", or "middle".

## Testing

The API has been tested with various combinations of inputs to ensure proper functionality and error handling.
