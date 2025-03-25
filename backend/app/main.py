from contextlib import asynccontextmanager
from typing import AsyncGenerator, Any

from fastapi import FastAPI

from app.api.routers import api_router
from app.bot.main import start_bot, stop_bot
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, None]:
    await start_bot()
    yield
    await stop_bot()


app = FastAPI(title=settings.app_title, lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello1": "FastAPI"}
