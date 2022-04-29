from pydantic.dataclasses import dataclass
from fastapi import Query
from typing import Optional, List
from app.models.standart_model import *


class SSD(StandardModel):
    pass


class SSDResponse(StandardModelResponse):
    pass
