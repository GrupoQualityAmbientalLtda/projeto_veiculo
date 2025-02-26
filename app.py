import streamlit as st

# telas
tela_login = st.Page(r'src\views\login\login.py', title='Tela de Login')
teste_pagina = st.Page(r'src\views\login\pagina_teste.py', title='Página de teste')
formulario = st.Page(r'src\views\formulario\view_formulario.py', title ='Formulário')

# barra de navegação
pagina = st.navigation([tela_login, teste_pagina, formulario])

# página selecionada
pagina.run()