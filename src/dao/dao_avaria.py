from src.models.avaria import Avaria
from src.database.db import create_session

class DaoAvaria:
    @classmethod
    def criar_avaria(cls, **kwargs):
        """
        Cria uma nova entrada de avaria no banco de dados.
        kwargs: Dicionário com os valores das colunas da tabela Avaria.
        """
        session = create_session()
        try:
            avaria = Avaria(**kwargs)
            session.add(avaria)
            session.commit()
            return avaria
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def obter_avaria_por_id(cls, id):
        """
        Obtém uma avaria pelo ID.
        """
        session = create_session()
        try:
            avaria = session.query(Avaria).filter(Avaria.id == id).first()
            return avaria
        finally:
            session.close()