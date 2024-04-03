import requests


def test_search_products():
    # Test with name and category filters
    response = requests.get(
        "/products/search", params={"name": "Product", "category": "Category A"})
    assert response.status_code == 200
    # Assuming there are 2 products matching the criteria
    assert len(response.json()) == 2

    # Test with price range filter
    response = requests.get(
        "/products/search", params={"min_price": 10.0, "max_price": 20.0})
    assert response.status_code == 200
    # Assuming there are 3 products within the price range
    assert len(response.json()) == 3

    # Test with all filters
    response = requests.get("/products/search", params={
                            "name": "Product", "category": "Category A", "min_price": 10.0, "max_price": 20.0})
    assert response.status_code == 200
    # Assuming there is 1 product matching all criteria
    assert len(response.json()) == 1

    # Test with no filters
    response = requests.get("/products/search")
    assert response.status_code == 200
    assert len(response.json()) == 4  # Assuming there are 4 products in total
