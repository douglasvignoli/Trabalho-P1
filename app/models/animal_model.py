from sqlalchemy import Column, Integer, String, Float
from app.database.postgres import Base


class Animal(Base):
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    raca = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float, nullable=False)
