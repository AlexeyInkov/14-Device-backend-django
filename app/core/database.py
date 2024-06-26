from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)

from app.core.config import settings
from app.models.orm_models import Model


my_engine = create_async_engine(settings.DB_URL, echo=settings.DB_ECHO)
my_session = async_sessionmaker(my_engine, expire_on_commit=False)


async def create_tables():
    async with my_engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with my_engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
