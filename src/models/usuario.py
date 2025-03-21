from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.database.db import Base
import enum

class PermissaoEnum(str, enum.Enum):
  MOTORISTA = 'motorista'
  GESTOR = 'gestor' # Pensar possibilidades de permissões de acesso ao sistema


class Usuario(Base):
  __tablename__ = 'usuarios'
  
  id = Column(Integer, primary_key=True)
  login = Column(String(255), nullable=False, unique=True)
  senha = Column(String(120), nullable=False)
  nome = Column(String(255), nullable=False)
  status = Column(Enum(PermissaoEnum), default=PermissaoEnum.GESTOR, nullable=False)