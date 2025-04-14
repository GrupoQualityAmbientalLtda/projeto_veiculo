import streamlit as st
from src.controller.controller_veiculo import ControllerVeiculo
import pandas as pd
# Status e Permissao
from src.models.veiculo import Veiculo, Status

from src.database.db import create_session
session = create_session()


st.title("Consulta de Veículos")
st.subheader("Pesquisa:")

@st.dialog(title='Criar Veículo')
def criar_veiculo():
    placa = st.text_input('Placa')
    modelo = st.text_input('Modelo')
    odometro = st.number_input(label="Quilometragem Inicial",value=0,min_value=0)
    avariado = st.toggle(label='Avariado?')
    cor = st.text_input('Cor')
    # lista_status = [status.value for status in Status]
    # status = st.selectbox('Status', lista_status)
    botao_cadastrar = st.button('Cadastrar Veículo')
    if botao_cadastrar:
        veiculo_salvo = ControllerVeiculo.criar_veiculo(placa = placa, 
                                                        modelo = modelo, 
                                                        odometro = odometro, 
                                                        avariado = avariado,
                                                        cor = cor
        )
        if veiculo_salvo:
            st.success('Veículo Cadastrado com Sucesso!')
        else:
            st.error('Erro ao cadastrar o veículo!')
if st.button("Novo Veículo"):
    criar_veiculo()

@st.cache_data
def carregar_dataframe():
    return ControllerVeiculo.carregar_dataframe_veiculos()

df = carregar_dataframe()
st.dataframe(df, use_container_width=True)