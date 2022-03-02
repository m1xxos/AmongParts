from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class GPU(BaseModel):
    name: str
    price: int = Query(..., ge=1)
    brand: str
    manufacture: str
    type: str
    interface: str
    video_chip: str
    frequency: int
    frequency_turbo: int
    tech_process: str
    video_memory: int
    memory_type: str
    memory_frequency: int
    memory_bus: str
    max_resolution: str
    sli: str
    ray_tracing: bool
    dlss: bool
    technology_support: str
    slot_vga: int
    slot_dvi: int
    slot_hdmi: int
    hdmi_version: str
    slot_display_port: int
    display_port_version: str
    power: str
    recommended_psu: int
    max_power: int
    length: int
    cooling: str
    photos: List[str] = None


@dataclass
class GPUSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
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
