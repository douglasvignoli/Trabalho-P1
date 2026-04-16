from fastapi import HTTPException, status
from typing import List

from app.schemas import AnimalCreate, AnimalUpdate, AnimalResponse
from app.repositories import (
    insert_animal,
    find_all_animals,
    find_animal_by_id,
    update_animal,
    delete_animal,
)


async def criar_animal(data: AnimalCreate) -> AnimalResponse:
    doc = await insert_animal(data.model_dump())
    return AnimalResponse(**doc)


async def listar_animais() -> List[AnimalResponse]:
    docs = await find_all_animals()
    return [AnimalResponse(**d) for d in docs]


async def buscar_animal(id: str) -> AnimalResponse:
    doc = await find_animal_by_id(id)
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Animal com ID '{id}' não encontrado."
        )
    return AnimalResponse(**doc)


async def atualizar_animal(id: str, data: AnimalUpdate) -> AnimalResponse:
    campos = {k: v for k, v in data.model_dump().items() if v is not None}

    if not campos:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum campo válido fornecido para atualização."
        )

    doc = await update_animal(id, campos)
    if not doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Animal com ID '{id}' não encontrado."
        )
    return AnimalResponse(**doc)


async def deletar_animal(id: str) -> None:
    removido = await delete_animal(id)
    if not removido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Animal com ID '{id}' não encontrado."
        )
