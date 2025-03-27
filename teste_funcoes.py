from src.models.avaria import Avaria
from src.models.destinos import Destino
from src.models.formulario import Formulario
from src.models.pergunta import Pergunta
from src.models.permissao import Permissao
from src.models.registros import Registro
from src.models.revisao import Revisao
from src.models.status_revisao import StatusRevisao
from src.models.usuario import Usuario
from src.models.veiculo import Veiculo
from src.models.formulario import TipoEnum
from src.database.db import *

from src.dao.dao_avaria import DaoAvaria
from src.dao.dao_formulario import DaoFormulario
from src.dao.dao_usuario import DaoUsuario
from src.dao.dao_veiculo import DaoVeiculo

from src.controller.controller_avaria import ControllerAvaria

from datetime import datetime

#drop_tables()
#create_tables()


def teste_criacao():
    session = create_session()

    id_usuario = 1
    id_veiculo = 3
    tipo = TipoEnum.ENTRADA
    id_revisao = 2
    data = datetime.strptime("2025-03-27", "%Y-%m-%d").date()

    formulario_criado = DaoFormulario.criar_formulario(
        session=session,
        id_usuario=id_usuario,
        id_veiculo=id_veiculo,
        tipo=tipo,
        data=data,
        id_revisao=id_revisao,
    )
    print(f"Forulário criado: {formulario_criado}")

    formulario_obtido = DaoFormulario.obter_formulario_por_id(session, formulario_criado.id)
    print(f"FOrmulário Obtido: {formulario_obtido}")

if __name__ == "__main__":
    teste_criacao()