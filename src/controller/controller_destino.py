from src.database.db import create_session
from src.models.destinos import Destino
from src.dao.dao_destinos import DaoDestino

class ControllerDestino:
    @classmethod
    def obter_todos_destinos(cls):
        with create_session() as session:
            try: 
                destinos = DaoDestino.obter_todos_destinos(session)
                return destinos
            except Exception as e:
                print(f'Erro inesperado: {e}')