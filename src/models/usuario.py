from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Usuario(Base):
  __tablename__ = 'usuarios'
  
  id = Column(Integer, primary_key=True)
  login = Column(String(255), nullable=False, unique=True)
  senha = Column(String(120), nullable=False)
  nome = Column(String(255), nullable=False)
  id_permissao = Column(Integer, ForeignKey('permissao.id'), nullable=False)
  