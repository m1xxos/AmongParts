from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Specs(BaseModel):
    motherboard: Optional[str] = None
    cpu: Optional[str] = None
    ram: Optional[str] = None
    ssd: Optional[str] = None
    hdd: Optional[str] = None
    gpu: Optional[str] = None
    psu: Optional[str] = None
    case: Optional[str] = None
    sound: Optional[str] = None
    cpu_cooling: Optional[str] = None
    case_cooling: Optional[str] = None
    enclosure: Optional[str] = None
    pci: Optional[str] = None
    optical: Optional[str] = None
    paste: Optional[str] = None


class Build(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    username: Optional[str] = None
    specifications: List = None
    link_name: Optional[str] = None


class BuildPost(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    specifications: Specs


class BuildResponse(BaseModel):
    amount: int
    data: list[Build]
