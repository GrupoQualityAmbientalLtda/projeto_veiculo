import streamlit as st
import pandas as pd
from src.controller.controller_formulario import ControllerFormulario
from src.controller.controller_destino import ControllerDestino
from src.database.db import create_session

st.title("Consulta de Formulários")
st.subheader("Listagem de todos os formulários")

@st.cache_data
def carregar_dataframe():
    with create_session() as session:
        formularios = ControllerFormulario.obter_todos_formularios()
        destinos = ControllerDestino.obter_todos_destinos()
        dataframe = pd.DataFrame([
            {
                "ID": formulario.id,
                "ID Veículo": formulario.id_veiculo,
                "ID Usuário": formulario.id_usuario,
                "Quilometragem": formulario.quilometragem,
                "Tipo": formulario.tipo,
                "Data": formulario.data.strftime('%d/%m/%Y %H:%M') if formulario.data else "",
                "Observações": formulario.observacao,
                "Destino": destino.destino
                #"Destino": formulario.destino.destino if formulario.destino else ""  # Acessando o destino
            }
            for formulario in formularios
            for destino in destinos
    ])
    dataframe['Seleção'] = False
    dataframe = dataframe.reindex(columns=[
        'Seleção', 'ID', 'ID Veículo', 'ID Usuário', 'Quilometragem',
        'Tipo', 'Data', 'Observações', 'Destino'
    ])
    return dataframe

dataframe_formulario = carregar_dataframe()
linha_selecionada = st.data_editor(dataframe_formulario, use_container_width=True)
