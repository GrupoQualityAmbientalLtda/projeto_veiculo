from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from src.database.db import Base
import enum

#class StatusEnum(str, enum.Enum): # SABER SE HÁ A NECESSIDADE DE MARCAR COMO CUMPRIDO OU NAO (A CAMINHO, EM PROCESSAMENTO)
  #CAMINHO = 'A Caminho'


class TipoEnum(str, enum.Enum):
  SAIDA = 'Saída'
  ENTRADA = 'Entrada'


class Formulario(Base):
  __tablename__='formularios'
  
  id = Column(Integer, primary_key=True)
  data = Column(DateTime,nullable=False)

  tipo = Column(Enum(TipoEnum), default=TipoEnum.ENTRADA, nullable=False)
  observacao = Column(String(255))

  # Chaves Estrangeiras
  id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
  id_veiculo = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
  id_revisao = Column(Integer, ForeignKey('revisao.id'), nullable = False)


  
  