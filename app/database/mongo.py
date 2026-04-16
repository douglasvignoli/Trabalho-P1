import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27018")
client = MongoClient(MONGO_URL)

db = client["aula_backend"]
animals_collection = db["animals"]