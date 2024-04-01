# FastAPI APIs Documentation

This repository contains documentation for several APIs built using FastAPI.

## User Registration API 👤

### Route: /register

- **Method**: POST
- **Description**: Create a new user account.
- **Request Body**:
  - username: string (required)
  - email: string (required, valid email format)
  - password: string (required, at least 8 characters, with at least one uppercase letter, one lowercase letter, one number, and one special character)
- **Response**:
  - Success: 201 Created
  - Error: 400 Bad Request

## Product Search API 🛒

### Route: /products

- **Method**: GET
- **Description**: Search products based on various criteria.
- **Query Parameters**:
  - product_name: string (optional)
  - category: string (optional)
  - min_price: float (optional)
  - max_price: float (optional)
- **Response**:
  - Success: 200 OK with a list of matching products
  - Error: 400 Bad Request

## Payment Processing API 💳

### Route: /payments

- **Method**: POST
- **Description**: Process a payment transaction.
- **Request Body**:
  - amount: float (required, positive value)
  - card_number: string (required, valid credit card number)
  - expiration_date: string (required, format: MM/YYYY, not expired)
  - cvv: string (required, 3 or 4 digits)
- **Response**:
  - Success: 200 OK with payment confirmation
  - Error: 400 Bad Request

## Vehicle Inventory API 🚗

### Route: /vehicles/{vehicle_id}

- **Method**: GET
- **Description**: Retrieve details of a specific vehicle.
- **Path Parameter**:
  - vehicle_id: integer (required, valid vehicle ID)
- **Query Parameters**:
  - make: string (optional)
  - model: string (optional)
  - min_price: float (optional)
  - max_price: float (optional)
- **Response**:
  - Success: 200 OK with vehicle details
  - Error: 404 Not Found if vehicle ID is invalid

## Flight Booking API ✈️

### Route: /flights/book

- **Method**: POST
- **Description**: Book a flight ticket.
- **Request Body**:
  - passenger_name: string (required)
  - passenger_age: integer (required, positive value)
  - contact_details: string (required, valid contact information)
  - origin: string (required)
  - destination: string (required)
  - date: string (required, format: YYYY-MM-DD)
  - seat_preference: string (required, valid options: window, aisle)
- **Response**:
  - Success: 200 OK with booking confirmation
  - Error: 400 Bad Request

## Event Booking API 🎟️

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

## Testing 🧪

Each API has been tested with various scenarios to ensure proper functionality and error handling.
