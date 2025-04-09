import streamlit as st

# Configuração da página
st.set_page_config(page_title="Consulta de Usuários", layout="wide")

# Título da página
st.title("Consulta de Usuários")

# Barra lateral
st.sidebar.header("Filtros")
nome = st.sidebar.text_input("Nome do Usuário")

# Corpo da página
st.subheader("Resultados da Consulta:")
