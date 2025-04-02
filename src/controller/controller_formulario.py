from src.dao.dao_formulario import DaoFormulario
from src.models.formulario import Formulario

from src.database.db import create_session

class ControllerFormulario:
    @classmethod
    def criar_formulario(cls, id_usuario, id_veiculo, id_revisao, data, id_tipo, observacao):
        session = create_session
        try: 
            formulario = DaoFormulario.criar_formulario(session, id_usuario,id_veiculo,id_tipo,id_revisao,data,observacao)
            session.flush()
        finally:
            session.close()
