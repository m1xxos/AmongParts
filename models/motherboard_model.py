from pydantic import BaseModel
from typing import Optional


class MotherBoard(BaseModel):
    name: str
    price: int
    brand: str
    type: str
    socket: str
    form_factor: str
    chipset: str
    memory_type: str
    memory_slots: int
    memory_speed: int
    memory_maximum_amount: int
    memory_channel: int
    pci_type: str
    pci_amount: int
    audio_chip: str
    audio_channel: str
    sata_amount: int
    m_2_amount: int
    m_2_type: str
    raid: bool = None
    slot_ps2: int
    slot_usb2: int
    slot_usb3: int
    slot_audio: int


class MotherBoardSearch(BaseModel):
    name: Optional[str] = None
    min_price: Optional[int] = None
    max_price: Optional[int] = None
    brand: Optional[str] = None
    type: Optional[str] = None
    socket: Optional[str] = None
    form_factor: Optional[str] = None
    chipset: Optional[str] = None
    memory_type: Optional[str] = None
    memory_slots: Optional[int] = None
    memory_speed: Optional[int] = None
    memory_maximum_amount: Optional[int] = None
    memory_channel: Optional[int] = None
    pci_type: Optional[str] = None
    pci_amount: Optional[int] = None
    audio_chip: Optional[str] = None
    audio_channel: Optional[str] = None
    sata_amount: Optional[int] = None
    m_2_amount: Optional[int] = None
    m_2_type: Optional[str] = None
    raid: Optional[bool] = None
    slot_ps2: Optional[int] = None
    slot_usb2: Optional[int] = None
    slot_usb3: Optional[int] = None
    slot_audio: Optional[int] = None




