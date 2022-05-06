from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Build(BaseModel):
    name: str = None

