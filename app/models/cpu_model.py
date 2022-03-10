from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class CPU(BaseModel):
    name: str
    price: int = Query(..., ge=1)
    brand: str
    type: str
    series: str
    core: str
    socket: str
    cpu_cores: int = Query(..., ge=1)
    cpu_threads: int = Query(..., ge=1)
    frequency: float
    frequency_turbo: float
    l3_cache: int
    architecture: str
    tech_process: str
    multiplier: bool
    tdp: int
    memory_type: str
    memory_speed: int
    memory_channel: int
    pci_version: str
    pci_lanes: int
    graphics: bool = None
    graphics_model: str = None
    graphics_speed: str = None
    photos: List[str] = None


@dataclass
class CPUSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    series: List[str] = Query(None)
    socket: List[str] = Query(None)
    min_frequency: Optional[int] = Query(None, ge=1)
    max_frequency: Optional[int] = Query(None, ge=1)
    cpu_cores: List[int] = Query(None)
    graphics: Optional[bool] = None
    multiplier: Optional[bool] = None
    pci_version: List[str] = Query(None)
    tdp: List[int] = Query(None)
