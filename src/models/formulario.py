from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Time
from sqlalchemy.orm import relationship
from src.database.db import Base
import enum
from src.models.usuario import Usuario
from src.models.veiculo import Veiculo
from src.models.revisao import Revisao

#class StatusEnum(str, enum.Enum): # SABER SE HÁ A NECESSIDADE DE MARCAR COMO CUMPRIDO OU NAO (A CAMINHO, EM PROCESSAMENTO)
  #CAMINHO = 'A Caminho'


class TipoEnum(str, enum.Enum):
  SAIDA = 'Saída'
  ENTRADA = 'Entrada'


class Formulario(Base):
  __tablename__='formularios'
  
  id = Column(Integer, primary_key=True)
  data = Column(DateTime,nullable=False)

  tipo = Column(Enum(TipoEnum), default=TipoEnum.SAIDA, nullable=False)
  observacao = Column(String(255))
  quilometragem = Column(Integer, nullable=False)


  # Chaves Estrangeiras
  id_usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
  id_veiculo = Column(Integer, ForeignKey('veiculos.id'), nullable=False)
  id_revisao = Column(Integer, ForeignKey('revisao.id'), nullable = False)

  usuario = relationship('Usuario', back_populates='formularios')
  veiculo = relationship('Veiculo', back_populates='formularios')
  revisao = relationship('Revisao', back_populates='formularios')

  destino = relationship("Destino", back_populates="formulario", cascade="all, delete-orphan")
  
  