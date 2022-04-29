from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class MarketItem(BaseModel):
    product_name: str = Field(..., alias='product name')
    product_link: str = Field(..., alias='product link')
    product_price: int = Field(..., alias='product price')


class StandardModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[str] = None
    reviews: Optional[Any] = None
    images: Optional[List[str]] = None
    videos: Optional[List[str]] = None
    specifications: Optional[dict] = None
    market: Optional[List[MarketItem]] = None


class StandardModelResponse(BaseModel):
    amount: int
    data: list[StandardModel]
