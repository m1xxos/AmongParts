from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class RAM(BaseModel):
    name: str = None
    price: int = None
    brand: str = None
    type: str = None
    photos: List[str] = None
    links: List[str] = None
    availability: bool = None
    memory_form: str = None
    memory_type: str = None
    memory_module: int = None
    memory_speed: int = None
    memory_channel: int = None
    module_amount: int = None
    combined_amount: int = None
    buffer: bool = None
    ecc: bool = None
    voltage: str = None
    timing: str = None
    latency: int = None


@dataclass
class RAMSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None, le=80000)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    availability: Optional[bool] = None
    memory_type: List[str] = Query(None)
    memory_form: List[str] = Query(None)
    memory_speed: List[int] = Query(None)
    ecc: Optional[bool] = None
    latency: List[int] = Query(None)
    voltage: List[str] = Query(None)
    memory_module: List[int] = Query(None)
