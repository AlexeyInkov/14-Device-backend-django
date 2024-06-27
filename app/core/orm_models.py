from datetime import datetime

from sqlalchemy import func, ForeignKey, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Model(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )


class Customer(Model):
    __tablename__ = "customers"

    name: Mapped[str]
    address: Mapped[str]


class MeteringUnit(Model):
    __tablename__ = "metering_units"

    customer: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    name: Mapped[str]


class DeviceRegistryNumber(Model):
    __tablename__ = "device_registry_numbers"
    registry_number: Mapped[int]


class DeviceType(Model):
    __tablename__ = "device_types"

    type: Mapped[str]
    name: Mapped[str]


class DeviceMod(Model):
    __tablename__ = "device_mods"

    name: Mapped[str]
    type_devise: Mapped[int] = mapped_column(ForeignKey("device_types.id"))


class DeviceInstallationPoint(Model):
    __tablename__ = "device_installation_points"

    name: Mapped[str]


class Device(Model):
    __tablename__ = "devices"

    registry_number: Mapped[int] = mapped_column(ForeignKey("registry_number.id"))
    device_type: Mapped[int] = mapped_column(ForeignKey("device_types.id"))
    device_mod: Mapped[int] = mapped_column(ForeignKey("device_mods.id"))
    factory_number: Mapped[str] = mapped_column(String(50))
    installation_point: Mapped[int] = mapped_column(
        ForeignKey("device_installation_points.id")
    )
    notes: Mapped[str] = mapped_column(String(100), nullable=True)
    metering_unit: Mapped[int] = mapped_column(ForeignKey("metering_units.id"))


class DeviceVerification(Model):
    __tablename__ = "device_verifications"

    device_id: Mapped[int] = mapped_column(ForeignKey("devices.id"))
    organization: Mapped[str] = mapped_column(String(50))
    verification_date: Mapped[datetime]
    valid_date: Mapped[datetime]
