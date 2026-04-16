from fastapi import FastAPI
from app.routers.animal_router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "FastAPI + Docker + Mongodb"}