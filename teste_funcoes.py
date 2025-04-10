from src.models.avaria import Avaria
from src.models.destinos import Destino
from src.models.formulario import Formulario
from src.models.registros import Registro
from src.models.revisao import Revisao
from src.models.usuario import Usuario
from src.models.veiculo import Veiculo
from src.models.destinos import Destino
from src.models.formulario import TipoEnum
from src.database.db import *

from src.dao.dao_avaria import DaoAvaria
from src.dao.dao_formulario import DaoFormulario
from src.dao.dao_usuario import DaoUsuario
from src.dao.dao_veiculo import DaoVeiculo
from src.dao.dao_destinos import DaoDestino

from datetime import datetime

#drop_tables()
#create_tables()

# Criação de veículo
# session = create_session()
# id = 1
# placa = 'KYN-4732'
# modelo = 'Strada'
# cor = 'Branca'
# odometro = '5000'
# avariado = True

# criar_veiculo = DaoVeiculo.criar_veiculo(session, placa, modelo, cor, odometro, avariado)



# obter_usuario = DaoUsuario.obter_usuario(session, 1)

# print(obter_usuario.login)


# CRIAÇÃO DE DESTINO

# id = 2
# destino = 'Somália'
# id_formulario = 1

# #criar_destino = DaoDestino.criar_destino(session, destino, id_formulario)

# obter_destinos = DaoDestino.obter_destinos(session, id)

# print(f"ID: {obter_destinos.id}, Destino: {obter_destinos.destino}, ID Formulário: {obter_destinos.id_formulario}")


# id = 4
# destino = 'Seychelles'
# id_formulario = 3

# criar_destino = DaoDestino.criar_destino(session, destino, id_formulario)

# destinos = DaoDestino.obter_destinos_por_formulario(session, id_formulario)
# # Exibição formatada
# print(f'\nDestinos vinculados ao ID do formulário: {id_formulario}')
# for d in destinos:
#     print(f'- ID do Destino: {d.id} | Destino: {d.destino}')

# FOR PARA FORMULARIOS COM MESMO ID

# deletar_destinos = DaoDestino.deletar_destinos(session, id)


