from src.models.revisao import Revisao
from src.database.db import create_session

class DaoRevisao:
    @classmethod
    def criar_revisao(cls, session, data, notificacao, id_veiculo, id_status):
        revisao = Revisao(data = data, notificacao = notificacao, id_veiculo = id_veiculo, id_status = id_status)
        session.add(revisao)
        session.commit()
        return revisao
    
    def obter_revisao(cls, session, id):
        revisao = session.query(Revisao).filter(Revisao.id == id).first()
        return revisao