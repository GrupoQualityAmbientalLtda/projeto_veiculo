from src.models.formulario import Formulario
from src.models.pergunta import Pergunta
from src.models.permissao import Permissao
from src.models.resposta import Resposta
from src.models.revisao import Revisao
from src.models.status_formulario import StatusFormulario
from src.models.status_pergunta import StatusPergunta
from src.models.status_revisao import StatusRevisao
from src.models.tipo import Tipo
from src.models.usuario import Usuario
from src.models.veiculo import Veiculo
from src.database.db import *

# drop_tables()
create_tables()

# É necessário importar todas as classes criadas, junto com o arquivo executável que cria as tabelas no caso db.py , e utilizar o create_tables(). Execute esse arquivo pelo VS CODE