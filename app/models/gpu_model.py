from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List
from app.models.standart_model import *


# class GPU(BaseModel):
#     name: str = None
#     price: int = None
#     brand: str = None
#     type: str = None
#     photos: List[str] = None
#     links: List[str] = None
#     availability: bool = None
#     manufacture: str = None
#     interface: str = None
#     video_chip: str = None
#     frequency: int = None
#     frequency_turbo: int = None
#     tech_process: str = None
#     video_memory: int = None
#     memory_type: str = None
#     memory_frequency: int = None
#     memory_bus: str = None
#     max_resolution: str = None
#     sli: str = None
#     ray_tracing: bool = None
#     dlss: bool = None
#     technology_support: str = None
#     slot_vga: int = None
#     slot_dvi: int = None
#     slot_hdmi: int = None
#     hdmi_version: str = None
#     slot_display_port: int = None
#     display_port_version: str = None
#     power: str = None
#     recommended_psu: int = None
#     max_power: int = None
#     length: int = None
#     cooling: str = None

class GPU(StandardModel):
    pass


@dataclass
class GPUSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    availability: Optional[bool] = None
    manufacture: List[str] = Query(None)
    video_chip: List[str] = Query(None)
    video_memory: List[int] = Query(None)
    memory_type: List[str] = Query(None)
    max_resolution: List[str] = Query(None)
    ray_tracing: Optional[bool] = None
    dlss: Optional[bool] = None
    interface: List[str] = Query(None)
    power: List[str] = Query(None)
    slot_vga: Optional[bool] = None
    slot_dvi: Optional[bool] = None
    slot_hdmi: Optional[bool] = None
    slot_display_port: Optional[bool] = None
    memory_bus: List[str] = Query(None)
    sli: List[str] = Query(None)
    min_length: Optional[int] = Query(None, ge=1)
    max_length: Optional[int] = Query(None, le=300)


class GPUResponse(StandardModelResponse):
    pass
