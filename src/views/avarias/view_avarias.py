import streamlit as st
import pandas as pd

from src.controller.controller_avaria import ControllerAvaria
from src.dao.dao_avaria import DaoAvaria
from src.models.avaria import Avaria
from src.database.db import create_session

st.title('Consulta de Avarias')
st.subheader("Pesquisa:")


@st.cache_data
def carregar_dataframe():
    return ControllerAvaria.carregar_dataframe_avarias()

# Carrega o DataFrame
dataframe_avaria = carregar_dataframe()

# Converte valores booleanos para strings "Verdadeiro" / "Falso"
dataframe_formatado = dataframe_avaria.copy()
for coluna in dataframe_formatado.columns:
    if dataframe_formatado[coluna].dtype == bool:
        dataframe_formatado[coluna] = dataframe_formatado[coluna].map({True: "Verdadeiro", False: "Falso"})

# Exibe o DataFrame
st.dataframe(dataframe_formatado, use_container_width=True, hide_index=True)

avarias = ControllerAvaria.listar_avarias_verdadeiras()

for avaria in avarias:
    chaves = [chave for chave in avaria.keys() if chave not in ("ID", "ID Formulário")]
    texto = ", ".join(chaves)
    st.text(f"Avarias encontradas: {texto}")