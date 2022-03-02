from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class PSU(BaseModel):
    name: str
    price: int = Query(..., ge=1)
    brand: str
    type: str
    form_factor: str
    atx_version: str
    wattage: int
    efficiency: int
    efficiency_standard: str
    mtbf: str
    detach_cables: bool
    braided_cables: bool
    power_cpu_motherboard: str
    power_gpu: str
    sata_amount: int
    molex_amount: int
    fdd_amount: int
    fan_size: str
    photos: List[str] = None


@dataclass
class PSUSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    detach_cables: Optional[bool] = None
    braided_cables: Optional[bool] = None
    min_wattage: Optional[int] = Query(None, ge=1)
    max_wattage: Optional[int] = Query(None)
    power_cpu_motherboard: List[str] = Query(None)
    efficiency_standard: List[str] = Query(None)
    fan_size: List[str] = Query(None)
    form_factor: List[str] = Query(None)
    power_gpu: List[str] = Query(None)

