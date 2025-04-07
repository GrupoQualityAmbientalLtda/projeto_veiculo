from sqlalchemy import Column, Integer, String, ForeignKey, delete
from src.database.db import Base

class Destino(Base):
    __tablename__='destinos'

    id = Column(Integer, primary_key = True)
    destino = Column(String(50), nullable = False)
    id_formulario = Column(Integer, ForeignKey('formularios.id'), nullable= False)
