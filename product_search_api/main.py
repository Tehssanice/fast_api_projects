from fastapi import FastAPI, Query
from typing import Optional, List
from models import Product, ProductSearchQuery
from services import search_products

app = FastAPI()


@app.get("/products/search", response_model=List[Product])
async def search_product(
    name: Optional[str] = Query(None, min_length=3, max_length=50),
    category: Optional[str] = Query(None, min_length=3, max_length=50),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0)
):
    query = ProductSearchQuery(name=name, category=category,
                               min_price=min_price, max_price=max_price)
    return search_products(query)
