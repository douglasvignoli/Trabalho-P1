import os
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "animaisdb")

client: AsyncIOMotorClient = None


async def connect_db():
    global client
    client = AsyncIOMotorClient(MONGO_URL)
    print(f"✅ Conectado ao MongoDB: {MONGO_URL}")


async def close_db():
    global client
    if client:
        client.close()
        print("🔌 Conexão encerrada.")


def get_collection(name: str) -> AsyncIOMotorCollection:
    return client[DB_NAME][name]
