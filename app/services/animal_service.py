from app.repositories.animal_repository import *
from bson import ObjectId

def format_animal(animal):
    animal["_id"] = str(animal["_id"])
    return animal

def get_all_animals_service():
    animals = get_all_animals()
    return [format_animal(animal) for animal in animals]

def create_animal_service(animal):
    result = create_animal(animal.model_dump())
    return {"message": "animal created", "id": str(result.inserted_id)}

def get_animal_by_id_service(animal_id):
    try:
        animal = get_animal_by_id(animal_id)

    except:
        return {"error": "Invalid id"}

    if not animal:
        return {"error": "animal not found"}
    return format_animal(animal)

def update_animal_service(animal_id, animal):
    try:
        result = update_animal(animal_id, animal.model_dump(exclude_none=True))

    except:
        return {"error": "Invalid id"}

    if result.matched_count == 0:
        return {"error": "animal not found"}
    return {"message": "Animal Updated"}

def delete_animal_service(animal_id):
    try:
        result = delete_animal(animal_id)

    except:
        return {"error": "Invalid id"}

    if result.deleted_count == 0:
        return {"error": "animal not found"}

    return {"message": "animal was deleted"}
