from app.database.mongo import animals_collection
from bson import ObjectId

def create_animal(animal_dict):
    return animals_collection.insert_one(animal_dict)

def get_all_animals():
    return list(animals_collection.find())

def get_animal_by_id(animal_id):
    return animals_collection.find_one({"_id": ObjectId(animal_id)})

def update_animal(animal_id, animal_dict):
    return animals_collection.update_one(
        {"_id": ObjectId(animal_id)},
        {"$set": animal_dict},
    )

def delete_animal(animal_id):
    return animals_collection.delete_one(
        {"_id": ObjectId(animal_id)}
    )
