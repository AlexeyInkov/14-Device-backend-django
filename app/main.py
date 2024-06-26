from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from loguru import logger

from api.v1.endpoints.pribor import router as auth_cookie_router
from app.core.config import settings
from app.core.database import create_tables, delete_tables
from app.utils.helpers import logging


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print("База готова")
    yield
    await delete_tables()
    print("База очищена")


app = FastAPI(lifespan=lifespan)

app.include_router(auth_cookie_router)
logger.configure(**settings.LOGGING_CONFIG)


@logging("run")
def main():
    pass


if __name__ == "__main__":
    main()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
