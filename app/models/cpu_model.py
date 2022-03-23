from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class CPU(BaseModel):
    name: str = None
    price: int = None
    brand: str = None
    type: str = None
    photos: List[str] = None
    links: List[str] = None
    availability: bool = None
    series: str = None
    core: str = None
    socket: str = None
    cpu_cores: int = Query(None, ge=1)
    cpu_threads: int = Query(None, ge=1)
    frequency: float = None
    frequency_turbo: float = None
    l3_cache: int = None
    architecture: str = None
    tech_process: str = None
    multiplier: bool = None
    tdp: int = None
    memory_type: str = None
    memory_speed: int = None
    memory_channel: int = None
    pci_version: str = None
    pci_lanes: int = None
    graphics: bool = None
    graphics_model: str = None
    graphics_speed: str = None


@dataclass
class CPUSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    availability: Optional[bool] = None
    series: List[str] = Query(None)
    socket: List[str] = Query(None)
    min_frequency: Optional[int] = Query(None, ge=1)
    max_frequency: Optional[int] = Query(None, ge=1)
    cpu_cores: List[int] = Query(None)
    graphics: Optional[bool] = None
    multiplier: Optional[bool] = None
    pci_version: List[str] = Query(None)
    tdp: List[int] = Query(None)
