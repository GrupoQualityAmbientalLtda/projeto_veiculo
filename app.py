import streamlit as st
from src.models.formulario import Formulario
from src.models.veiculo import Veiculo
from src.models.revisao import Revisao
from src.models.destinos import Destino
from src.models.usuario import Usuario
from src.controller.controller_usuario import ControllerUsuario

# telas
tela_login = st.Page(r'src\views\login\view_login.py', title='Tela de Login')
tela_cadastro = st.Page(r'src\views\cadastro\view_cadastro.py', title='Tela de Cadastro')
formulario = st.Page(r'src\views\formulario\view_formulario.py', title ='Formulário')
consulta_formularios = st.Page(r'src\views\consulta_formulario\view_consulta_formularios.py', title = 'Consulta de Formulários')
revisao = st.Page(r'src\views\revisao\view_revisao.py', title='Revisão')
usuarios = st.Page(r'src\views\usuarios\view_usuarios.py', title='Consulta de Usuários')
veiculos = st.Page(r'src\views\veiculos\view_veiculos.py', title='Criação de Veículos')

# # if not st.experimental_user.is_logged_in:
# #     if st.button("Log in"):
# #         st.login()
# # else:
# #     if st.button("Log out"):
# #         st.logout()
# #     st.write(f"Hello, {st.experimental_user.name}!")

# usuarios = {'waldemberg': '123456', 'lucas': '123456'}

# if 'logado' not in st.session_state:
#     st.session_state['logado'] = None


# if st.session_state.logado is None:
#     with st.form(key='Login'):
#         login = st.text_input('Login')
#         senha = st.text_input('Senha', type='password')
#         logar = st.form_submit_button('Logar')
#         if logar:
#             if usuarios.get(login) == senha:
#                 st.session_state.logado = login
#                 st.rerun()
#             else:
#                 st.error('Login ou senha inválidos')
# else:
#     # barra de navegação
#     st.text('O usuário está logado')

# verificando se existe usuário na sessão
if 'usuario' not in st.session_state:
    st.session_state.usuario = None

if not st.user.is_logged_in:
    with st.form('Login_2'):
        st.image("imgs/logo.png")
        login = st.text_input('Login', placeholder="Digite seu login")
        senha = st.text_input('Senha', type="password", placeholder="Digite sua senha")
        
        fazer_login = st.form_submit_button("Fazer Login")
    
        if fazer_login:
            usuario = ControllerUsuario.verificar_login(login, senha)
            print(usuario)
            if usuario:
                st.session_state.usuario = usuario
                st.rerun()

if st.session_state.get('usuario') and not st.user.is_logged_in:
    st.login()
if st.user.is_logged_in:
    pagina = st.navigation([formulario, consulta_formularios, usuarios, veiculos])
        # página selecionada
    pagina.run()
    with st.sidebar:
        if st.button("Log out"):
            st.logout()

