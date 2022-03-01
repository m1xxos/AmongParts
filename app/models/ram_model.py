from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class RAM(BaseModel):
    name: str
    price: int = Query(..., ge=1)
    brand: str
    type: str
    memory_form: str
    memory_type: str
    memory_module: int
    memory_speed: int
    memory_channel: int
    module_amount: int
    combined_amount: int
    buffer: bool
    ecc: bool
    voltage: str
    timing: str
    latency: int


@dataclass
class RAMSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None, le=80000)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    memory_type: List[str] = Query(None)
    memory_form: List[str] = Query(None)
    memory_speed: List[int] = Query(None)
    ecc: Optional[bool] = None
    latency: List[int] = Query(None)
    voltage: List[str] = Query(None)
    memory_module: List[int] = Query(None)
