import streamlit as st

# telas
tela_login = st.Page(r'src\views\login\view_login.py', title='Tela de Login')
formulario = st.Page(r'src\views\formulario\view_formulario.py', title ='Formulário')
revisao = st.Page(r'src\views\revisao\view_revisao.py', title='Revisão')

# barra de navegação
pagina = st.navigation([tela_login, formulario, revisao])

# página selecionada
pagina.run()