from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.database.db import Base

class Revisao(Base):
  __tablename__ = 'revisao'
  
  id = Column(Integer, primary_key=True)
  data = Column(DateTime,nullable=False)
  notificacao = Column(String(120), nullable=False)
  id_veiculo = Column(String(7), ForeignKey('veiculos.id'), nullable=False)
  id_status = Column(String(120), ForeignKey('status_revisao.id'), nullable=False)