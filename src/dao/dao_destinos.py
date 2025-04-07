from src.models.destinos import Destino
from src.database.db import create_session

class DaoDestino:
    @classmethod

    def criar_destino(cls, session, destino, id_formulario):
        destinos = Destino(destino = destino, id_formulario = id_formulario)
        session.add(destinos)
        session.commit()
        return destinos
    @classmethod
    def obter_destinos(cls, session, id):
        destinos = session.query(Destino).filter(Destino.id == id).first()
        return destinos
    @classmethod
    def obter_destinos_por_formulario(cls, session, id_formulario):
        destinos_formulario = session.query(Destino).filter(Destino.id_formulario == id_formulario).all()
        return destinos_formulario
    @classmethod
    def deletar_destinos(cls,session,id):
        session = create_session()
        delete_destinos = session.query(Destino).filter(Destino.id == id).first()
        session.delete(delete_destinos)
        session.commit()
        return delete_destinos