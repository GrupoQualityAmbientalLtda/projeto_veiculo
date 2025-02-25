from sqlalchemy import Column, Integer, String, ForeignKey, datetime
from sqlalchemy.orm import relationship
from src.database.db import Base

class Veiculo(Base):
  __tablename__ = 'veiculos'
  
  placa = Column(String(7),primary_key=True)
  modelo = Column(String(120), nullable=False)
  cor = Column(String(50), nullable=False)
  odometro = Column(Integer(), nullable=False)