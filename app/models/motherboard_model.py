from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class MotherBoard(BaseModel):
    name: str = None
    price: int = None
    brand: str = None
    type: str = None
    photos: List[str] = None
    links: List[str] = None
    availability: bool = None
    socket: str = None
    form_factor: str = None
    chipset: str = None
    memory_type: str = None
    memory_slots: int = None
    memory_speed: str = None
    memory_maximum: str = None
    memory_channel: str = None
    pci_2: Optional[int] = None
    pci_3: Optional[int] = None
    pci_4: Optional[int] = None
    pci_5: Optional[int] = None
    audio_chip: Optional[str] = None
    audio_channel: Optional[str] = None
    sata_amount: int = None
    m_2_amount: Optional[int] = None
    raid: Optional[bool] = None
    optane: Optional[bool] = None
    ethernet: str = None
    slot_ps2: Optional[str] = None
    slot_usb2: Optional[int] = None
    slot_usb3: Optional[int] = None
    slot_usbc: Optional[int] = None
    slot_display_port: Optional[int] = None
    slot_vga: Optional[int] = None
    slot_dvi: Optional[int] = None
    slot_hdmi: Optional[int] = None
    slot_thunderbolt: Optional[int] = None
    wi_fi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    sli: Optional[str] = None
    power: str = None


@dataclass
class MotherBoardSearch:
    min_price: Optional[int] = Query(None, ge=1)
    max_price: Optional[int] = Query(None)
    type: List[str] = Query(None)
    brand: List[str] = Query(None)
    socket: List[str] = Query(None)
    memory_slots: List[int] = Query(None)
    chipset: List[str] = Query(None)
    form_factor: List[str] = Query(None)
    pci_2: Optional[bool] = None
    pci_3: Optional[bool] = None
    pci_4: Optional[bool] = None
    pci_5: Optional[bool] = None
    raid: Optional[bool] = None
    optane: Optional[bool] = None
    wi_fi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    memory_type: Optional[str] = None
    sata: Optional[bool] = None
    m_2: Optional[bool] = None
    sli: Optional[str] = None



