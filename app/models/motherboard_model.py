from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List


class MotherBoard(BaseModel):
    name: str
    price: int = Query(..., ge=1)
    brand: str
    type: str
    socket: str
    form_factor: str
    chipset: str
    memory_type: str
    memory_slots: int
    memory_speed: int
    memory_maximum: int
    memory_channel: int
    pci_2: Optional[int]
    pci_3: Optional[int]
    pci_4: Optional[int]
    pci_5: Optional[int]
    audio_chip: str
    audio_channel: str
    sata_amount: int
    m_2_amount: int
    raid: Optional[bool] = None
    optane: Optional[bool] = None
    ethernet: str
    slot_ps2: Optional[int] = None
    slot_usb2: Optional[int] = None
    slot_usb3: Optional[int] = None
    slot_usbc: Optional[int] = None
    slot_display_port: Optional[int] = None
    slot_vga: Optional[int] = None
    slot_com: Optional[int] = None
    slot_lpt: Optional[int] = None
    slot_hdmi: Optional[int] = None
    slot_thunderbolt: Optional[int] = None
    wi_fi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    sli: Optional[str] = None
    power: str
    photos: List[str] = None


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



