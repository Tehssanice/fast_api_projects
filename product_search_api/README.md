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
