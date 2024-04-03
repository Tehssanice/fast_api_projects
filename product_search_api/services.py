from typing import List
from models import Product, ProductSearchQuery

# Dummy product data (replace with your actual product data)
products = [
    Product(id=1, name="Product 1", category="Category A", price=10.0),
    Product(id=2, name="Product 2", category="Category B", price=20.0),
    Product(id=3, name="Product 3", category="Category A", price=15.0),
    Product(id=4, name="Product 4", category="Category C", price=25.0),
]


def search_products(query: ProductSearchQuery) -> List[Product]:
    result = products

    if query.name:
        result = [p for p in result if query.name.lower() in p.name.lower()]

    if query.category:
        result = [p for p in result if query.category.lower()
                  in p.category.lower()]

    if query.min_price:
        result = [p for p in result if p.price >= query.min_price]

    if query.max_price:
        result = [p for p in result if p.price <= query.max_price]

    return result
