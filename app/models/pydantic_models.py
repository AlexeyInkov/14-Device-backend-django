from datetime import datetime

from pydantic import BaseModel


class BaseTypeDevice(BaseModel):
    type: str


class CreateTypeDevice(BaseTypeDevice):
    pass


class TypeDevice(BaseTypeDevice):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime


class BaseModDevice(BaseModel):
    name: str
    type_devise: str


class CreateModDevice(BaseModDevice):
    pass


class ModDevice(BaseModDevice):
    id: int
    created_at: datetime
    updated_at: datetime
