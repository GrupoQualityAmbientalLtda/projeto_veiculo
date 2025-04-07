from src.models.registros import Registro
from src.database.db import create_session

class DaoRegistro:
    @classmethod
    def criar_registro(cls, session, foto, id_avaria):
        registros = Registro(foto = foto, id_avaria = id_avaria)
        session.add(registros)
        session.commit()
        return registros
    
    @classmethod
    def obter_registros(cls, session, id_avaria):
        registros = session.query(Registro).filter(Registro.id_avaria == id_avaria).all()
        return registros
    
    # Terminar inserção de Imagens