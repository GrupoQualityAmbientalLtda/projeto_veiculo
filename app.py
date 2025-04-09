import streamlit as st

# telas
tela_login = st.Page(r'src\views\login\view_login.py', title='Tela de Login')
tela_cadatro = st.Page(r'src\views\cadastro\view_cadastro.py', title='Tela de Cadastro')
formulario = st.Page(r'src\views\formulario\view_formulario.py', title ='Formulário')
revisao = st.Page(r'src\views\revisao\view_revisao.py', title='Revisão')
usuarios = st.Page(r'src\views\usuarios\usuarios.py', title='Consulta de Usuários')

# barra de navegação
pagina = st.navigation([tela_cadatro,tela_login, formulario, revisao, usuarios],)

# página selecionada
pagina.run()