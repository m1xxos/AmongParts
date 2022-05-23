from pydantic import BaseModel


class FormModel(BaseModel):
    name: str
    email: str
    phone_number: str
    description: str
    price: float
    type: str
