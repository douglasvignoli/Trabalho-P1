from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class EspecieEnum(str, Enum):
    mamifero = "Mamífero"
    ave = "Ave"
    reptil = "Réptil"
    anfibio = "Anfíbio"
    peixe = "Peixe"
    invertebrado = "Invertebrado"


class AnimalCreate(BaseModel):
    nome: str = Field(..., min_length=1, max_length=100, description="Nome do animal")
    especie: EspecieEnum = Field(..., description="Classificação da espécie")
    idade_anos: float = Field(..., ge=0, description="Idade em anos")
    peso_kg: float = Field(..., gt=0, description="Peso em quilogramas")


class AnimalUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=100)
    especie: Optional[EspecieEnum] = None
    idade_anos: Optional[float] = Field(None, ge=0)
    peso_kg: Optional[float] = Field(None, gt=0)


class AnimalResponse(BaseModel):
    id: str = Field(..., description="ID único gerado pelo MongoDB")
    nome: str
    especie: EspecieEnum
    idade_anos: float
    peso_kg: float
