from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_search_products():
    # Test case: Search for a product by name
    response = client.get(
        "/search?name=air%20conditioner&price_range=20-40")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "rice", "category": "food", "price": 95.0},
        {"name": "rice", "category": "food", "price": 15.0}
    ]

#     # Test case: Search for products in a specific category
#     response = client.get(
#         "/products/search?category=elctronics")
#     assert response.status_code == 200
#     assert response.json()["category"] == "electronics"

#  # Test case: Search for products in a price range
#     response = client.get("/products/search?price_range=20-40")
#     assert response.status_code == 200
#     assert response.json()["price"] <= 35

# #  Test case: Search for products with a combination of criteria
#     response = client.get(
#         "/products/search?name=crop-top&category=clothing&price_range=30-70")
#     assert response.status_code == 200
#     assert response.json()["name"] == "crop-top"
#     assert response.json()["category"] == "clothing"
#     assert response.json()["price"] <= 45


# # Test case: Product not found
#     response = client.get("products/search")
#     assert response.status_code == 200
