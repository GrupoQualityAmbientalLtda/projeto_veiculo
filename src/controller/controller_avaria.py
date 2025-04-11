from src.dao.dao_avaria import DaoAvaria
from src.database.db import create_session

class ControllerAvaria:
    @classmethod
    def criar_avaria(cls, id_formulario: int, **kwargs):
        """
        Cria uma avaria no banco associada a um formulário.
        """
        with create_session() as session:
            return DaoAvaria.criar_avaria(session, id_formulario=id_formulario, **kwargs)
