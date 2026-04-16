from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status
from typing import Optional

from app.database import get_collection

COLLECTION = "animais"


def _to_dict(doc: dict) -> dict:
    """Converte _id ObjectId em string."""
    doc["id"] = str(doc.pop("_id"))
    return doc


def _parse_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"ID inválido: '{id}'"
        )


async def insert_animal(data: dict) -> dict:
    collection = get_collection(COLLECTION)
    result = await collection.insert_one(data)
    doc = await collection.find_one({"_id": result.inserted_id})
    return _to_dict(doc)


async def find_all_animals() -> list[dict]:
    collection = get_collection(COLLECTION)
    animais = []
    async for doc in collection.find():
        animais.append(_to_dict(doc))
    return animais


async def find_animal_by_id(id: str) -> Optional[dict]:
    collection = get_collection(COLLECTION)
    oid = _parse_id(id)
    doc = await collection.find_one({"_id": oid})
    if not doc:
        return None
    return _to_dict(doc)


async def update_animal(id: str, campos: dict) -> Optional[dict]:
    collection = get_collection(COLLECTION)
    oid = _parse_id(id)
    result = await collection.update_one({"_id": oid}, {"$set": campos})
    if result.matched_count == 0:
        return None
    doc = await collection.find_one({"_id": oid})
    return _to_dict(doc)


async def delete_animal(id: str) -> bool:
    collection = get_collection(COLLECTION)
    oid = _parse_id(id)
    result = await collection.delete_one({"_id": oid})
    return result.deleted_count > 0
