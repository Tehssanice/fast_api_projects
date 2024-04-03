from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    category: str
    price: float


class ProductQueryParams(BaseModel):
    name: Optional[str]
    category: Optional[str]
    min_price: Optional[float]
    max_price: Optional[float]
