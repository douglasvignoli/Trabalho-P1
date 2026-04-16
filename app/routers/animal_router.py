from fastapi import APIRouter, status
from typing import List

from app.schemas import AnimalCreate, AnimalUpdate, AnimalResponse
from app.services import (
    criar_animal,
    listar_animais,
    buscar_animal,
    atualizar_animal,
    deletar_animal,
)

router = APIRouter(prefix="/animais", tags=["Animais"])


@router.post(
    "",
    response_model=AnimalResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar um novo animal",
)
async def create(animal: AnimalCreate):
    return await criar_animal(animal)


@router.get(
    "",
    response_model=List[AnimalResponse],
    summary="Listar todos os animais",
)
async def read_all():
    return await listar_animais()


@router.get(
    "/{id}",
    response_model=AnimalResponse,
    summary="Buscar animal por ID",
)
async def read_one(id: str):
    return await buscar_animal(id)


@router.put(
    "/{id}",
    response_model=AnimalResponse,
    summary="Atualizar animal por ID",
)
async def update(id: str, dados: AnimalUpdate):
    return await atualizar_animal(id, dados)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Remover animal por ID",
)
async def delete(id: str):
    await deletar_animal(id)
