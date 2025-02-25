from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database.db import Base

class StatusFormulario(Base):
  __tablename__ = 'status_formulario'
  
  id = Column(Integer(), primary_key=True)
  nome = Column(String(120), nullable=False)