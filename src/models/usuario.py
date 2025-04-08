from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from src.database.db import Base
import enum

class PermissaoEnum(str, enum.Enum):
  MOTORISTA = 'motorista'
  GESTOR = 'gestor' # Pensar possibilidades de permissões de acesso ao sistema

class Status(str, enum.Enum):
  ATIVO = 'ativo'
  INATIVO = 'inativo'


class Usuario(Base):
  __tablename__ = 'usuarios'
  
  id = Column(Integer, primary_key=True)
  login = Column(String(255), nullable=False, unique=True)
  senha = Column(String(120), nullable=False)
  nome = Column(String(255), nullable=False)
  permissao = Column(Enum(PermissaoEnum), default=PermissaoEnum.GESTOR, nullable=False)
  status = Column(Enum(Status), default=Status.ATIVO, nullable=False)
  