from fastapi import APIRouter, Query

router = APIRouter()

fake_products_db = [
    {"name": "air conditioner", "category": "electronics", "price": 50.0},
    {"name": "mobile phone", "category": "electronics", "price": 80.0},
    {"name": "crop-top", "category": "clothing", "price": 25.0},
    {"name": "rice", "category": "food", "price": 95.0},
    {"name": "air conditioner", "category": "electronics", "price": 30.0},
    {"name": "rice", "category": "food", "price": 15.0}

]


@router.get("/search")
async def search_product(name: str = Query(None, description="The name of the product"), category: str = Query(None), price_range: str = Query("0-100")):

    searched_products = []

    min_price, max_price = map(float, price_range.split("-"))

    for product in fake_products_db:
        if product['name'] == name:
            searched_products.append(product)

        if product["category"] == category:
            searched_products.append(product)

        # if min_price <= product["price"] <= max_price:
        #     searched_products.append(product)

    return searched_products
