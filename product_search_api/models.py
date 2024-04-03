from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float


class ProductSearchQuery(BaseModel):
    name: Optional[str]
    category: Optional[str]
    min_price: Optional[float]
    max_price: Optional[float]
