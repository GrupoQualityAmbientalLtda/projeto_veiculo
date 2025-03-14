# NÃO SERÁ UTILIZADO

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Pergunta(Base):
  __tablename__ = 'perguntas'
  
  id = Column(Integer, primary_key=True)
  texto = Column(String(120), nullable=False)
  id_status = Column(String(7), ForeignKey('status_formulario.id'), nullable=False)
  id_tipo = Column(String(7), ForeignKey('tipo.id'), nullable=False)
  