from datetime import datetime

from sqlalchemy import func, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Model(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())


class DeviceType(Model):
    __tablename__ = "device_types"

    type: Mapped[str]
    name: Mapped[str]


class DeviceMod(Model):
    __tablename__ = "device_mods"

    name: Mapped[str]
    type_devise: Mapped[int] = mapped_column(ForeignKey("device_types.id"))
