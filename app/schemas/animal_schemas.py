from pydantic import BaseModel, Field
from typing import Optional

class Animal(BaseModel):
    nome: str
    especie: str
    raca: str
    idade: int
    peso: float

class AnimalUpdate(BaseModel):
    nome: Optional[str] = Field(None, example=None)
    especie: Optional[str] = Field(None, example=None)
    raca: Optional[str] = Field(None, example=None)
    idade: Optional[int] = Field(None, example=None)
    peso: Optional[float] = Field(None, example=None)
