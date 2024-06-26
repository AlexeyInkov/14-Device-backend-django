from sqlalchemy import select

from app.core.database import my_session
from app.models.orm_models import DeviceType
from app.models.pydantic_models import CreateTypeDevice, TypeDevice


class DeviceTypeRepository:
    @classmethod
    async def add_device_type(cls, device_type: CreateTypeDevice) -> int:
        async with my_session as session:
            data = device_type.model_dump()
            new_device_type = DeviceType(**data)
            session.add(new_device_type)
            await session.flush()
            await session.commit()
            return new_device_type.id

    @classmethod
    async def get_device_types(cls) -> list[TypeDevice]:
        async with my_session as session:
            query = select(DeviceType)
            result = await session.execute(query)
            device_type_models = result.scalars().all()
            device_types = [
                TypeDevice.model_validate(device_type_model)
                for device_type_model in device_type_models
            ]
            return device_types
