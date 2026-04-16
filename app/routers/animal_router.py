from fastapi import APIRouter
from app.schemas.animal_schemas import Animal, AnimalUpdate
from app.services.animal_service import *

router = APIRouter()

@router.get("/animal")
def list_animals():
    return get_all_animals_service()

@router.get("/hello")
def hello():
    return "Hello World!"

@router.post("/animals")
def create_animal(animal: Animal):
    return create_animal_service(animal)

@router.get("/animals/{animal_id}")
def get_animal(animal_id: str):
    return get_animal_by_id_service(animal_id)

@router.put("/animals/{animal_id}")
def update_animal(animal_id: str, animal: AnimalUpdate):
    return update_animal_service(animal_id, animal)

@router.delete("/animals/{animal_id}")
def delete_animal(animal_id: str):
    return delete_animal_service(animal_id)
