from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List
from app.models.standart_model import *


class PSU(StandardModel):
    pass


class PSUResponse(StandardModelResponse):
    pass


# class PSU(BaseModel):
#     name: str = None
#     price: int = None
#     brand: str = None
#     type: str = None
#     photos: List[str] = None
#     links: List[str] = None
#     availability: bool = None
#     form_factor: str = None
#     atx_version: str = None
#     wattage: int = None
#     efficiency: int = None
#     efficiency_standard: str = None
#     mtbf: str = None
#     detach_cables: bool = None
#     braided_cables: bool = None
#     power_cpu_motherboard: str = None
#     power_gpu: str = None
#     sata_amount: int = None
#     molex_amount: int = None
#     fdd_amount: int = None
#     fan_size: str = None


@dataclass
class PSUSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    availability: Optional[bool] = None
    detach_cables: Optional[bool] = None
    braided_cables: Optional[bool] = None
    min_wattage: Optional[int] = Query(None, ge=1)
    max_wattage: Optional[int] = Query(None)
    power_cpu_motherboard: List[str] = Query(None)
    efficiency_standard: List[str] = Query(None)
    fan_size: List[str] = Query(None)
    form_factor: List[str] = Query(None)
    power_gpu: List[str] = Query(None)

