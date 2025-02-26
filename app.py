import streamlit as st

# telas
tela_login = st.Page(r'src\views\login\login.py', title='Tela de Login')
formulario = st.Page(r'src\views\formulario\view_formulario.py', title ='Formulário')

# barra de navegação
pagina = st.navigation([tela_login, formulario])

# página selecionada
pagina.run()