from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database.db import Base

class StatusRevisao(Base):
  __tablename__ = 'status_revisao'
  
  id = Column(Integer(), primary_key=True)
  nome = Column(String(120), nullable=False)