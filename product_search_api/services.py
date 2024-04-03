from typing import List
from models import Product, ProductQueryParams

# Dummy database
fake_products_db = [
    Product(name="Product A", category="Category A", price=10.0),
    Product(name="Product B", category="Category B", price=15.0),
    Product(name="Product C", category="Category A", price=20.0),
    Product(name="Product D", category="Category C", price=25.0),
]


def search_products(params: ProductQueryParams) -> List[Product]:
    filtered_products = fake_products_db

    if params.name:
        filtered_products = [
            p for p in filtered_products if params.name.lower() in p.name.lower()]

    if params.category:
        filtered_products = [
            p for p in filtered_products if params.category.lower() in p.category.lower()]

    if params.min_price:
        filtered_products = [
            p for p in filtered_products if p.price >= params.min_price]

    if params.max_price:
        filtered_products = [
            p for p in filtered_products if p.price <= params.max_price]

    return filtered_products
