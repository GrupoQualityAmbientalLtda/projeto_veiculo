from sqlalchemy import Column, Integer, String, ForeignKey, datetime
from sqlalchemy.orm import relationship
from src.database.db import Base

class Tipo(Base):
  __tablename__ = 'tipo'
  
  id = Column(Integer(),primary_key=True,)
  tipo = Column(String(120), nullable=False)