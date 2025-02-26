from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from src.database.db import Base
import enum

class TipoEnum(str, enum.Enum):
  SAIDA = 'Saída'
  ENTRADA = 'Entrada'


class Formulario(Base):
  __tablename__='formularios'
  
  id = Column(Integer, primary_key=True)
  data = Column(DateTime,nullable=False)

  # Chaves Estrangeiras
  id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
  id_veiculo = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
  id_tipo = Column(Integer, ForeignKey('tipo.id'), nullable=False)
  id_status = Column(Integer, ForeignKey('status_formulario.id'), nullable=False)
  