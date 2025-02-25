from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Permissao(Base):
  __tablename__ = 'permissao'
  
  id = Column(Integer, primary_key=True)
  nome = Column(String(255), nullable=False)