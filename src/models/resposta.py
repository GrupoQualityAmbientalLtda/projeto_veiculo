from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database.db import Base

class Resposta(Base):
  __tablename__ = 'respostas'
  
  id = Column(Integer, primary_key=True)
  resultado = Column(String(120), nullable=False)
  id_pergunta = Column(String(7), ForeignKey('perguntas.id'), nullable=False)