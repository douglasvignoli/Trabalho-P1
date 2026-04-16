from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database import connect_db, close_db
from app.routers import router as animal_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    yield
    await close_db()


app = FastAPI(
    title="API de Animais 🐾",
    description="CRUD de animais com FastAPI e MongoDB",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(animal_router)
