from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class MarketItem(BaseModel):
    product_name: str = Field(..., alias='product name')
    product_link: str = Field(..., alias='product link')
    product_price: int = Field(..., alias='product price')


class SSD(BaseModel):
    name: str
    description: str
    rating: Any
    reviews: Any
    images: List[str]
    videos: List
    specifications: dict
    market: List[MarketItem]
