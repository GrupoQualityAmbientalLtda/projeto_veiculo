from sqlalchemy import Integer, Column, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Registro(Base):
    __tablename__='registros'

    id = Column(Integer, primary_key=True)

    foto = Column(LargeBinary, nullable=False)
    id_avaria = Column(Integer, ForeignKey('avarias.id'))
    id_formulario = Column(Integer, ForeignKey('formularios.id'), nullable=False)