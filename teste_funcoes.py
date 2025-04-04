from src.models.avaria import Avaria
from src.models.destinos import Destino
from src.models.formulario import Formulario
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




session = create_session()

# obter_usuario = DaoUsuario.obter_usuario(session, 1)

# print(obter_usuario.login)

obter_avaria = DaoAvaria.obter_avaria(session, 2)

print(f"Avaria obtida: {obter_avaria}")

session.close()

