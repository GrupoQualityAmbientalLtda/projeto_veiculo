import streamlit as st
from src.models.formulario import Formulario
from src.models.veiculo import Veiculo
from src.models.revisao import Revisao
from src.models.destinos import Destino
from src.models.usuario import Usuario

# telas
tela_login = st.Page(r'src\views\login\view_login.py', title='Tela de Login')
tela_cadastro = st.Page(r'src\views\cadastro\view_cadastro.py', title='Tela de Cadastro')
formulario = st.Page(r'src\views\formulario\view_formulario.py', title ='Formulário')
consulta_formularios = st.Page(r'src\views\consulta_formulario\view_consulta_formularios.py', title = 'Consulta de Formulários')
revisao = st.Page(r'src\views\revisao\view_revisao.py', title='Revisão')
usuarios = st.Page(r'src\views\usuarios\view_usuarios.py', title='Consulta de Usuários')
veiculos = st.Page(r'src\views\veiculos\view_veiculos.py', title='Criação de Veículos')

# barra de navegação
pagina = st.navigation([tela_login, formulario, revisao, consulta_formularios, usuarios, veiculos],)

# página selecionada
pagina.run()