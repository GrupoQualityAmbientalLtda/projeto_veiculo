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
    lista_status = [status.value for status in Status]
    status = st.selectbox('Status', lista_status)
    botao_cadastrar = st.button('Cadastrar Veículo')
    if botao_cadastrar:
        veiculo_salvo = ControllerVeiculo.criar_veiculo(placa = placa, 
                                                        modelo = modelo, 
                                                        odometro = odometro, 
                                                        avariado = avariado,
                                                        cor = cor,
                                                        status = status
        )
        if veiculo_salvo:
            st.success('Veículo Cadastrado com Sucesso!')
            st.cache_data.clear()
            st.rerun()
        else:
            st.error('Erro ao cadastrar o veículo!')
if st.button("Novo Veículo"):
    criar_veiculo()

@st.dialog(title='Editar Veículo')
def atualizar_veiculo():
    id = st.number_input('ID',value=0,min_value=0)
    nova_placa = st.text_input('Nova Placa')
    novo_modelo = st.text_input('Novo Modelo')
    nova_cor = st.text_input('Nova Cor')
    novo_odometro = st.number_input(label="Quilometragem Inicial",value=0,min_value=0)
    novo_avariado = st.toggle(label='Avariado?')
    lista_status = [status.value for status in Status]
    novo_status = st.selectbox('Novo Status', lista_status)

    botao_atualizar = st.button('Atualizar Usuário', key='botao_atualizar_usuario')

    if botao_atualizar:
        veiculo_atualizado = ControllerVeiculo.atualizar_veiculo_pelo_id(id = id,
                                                                         nova_placa = nova_placa,
                                                                         novo_modelo = novo_modelo,
                                                                         nova_cor = nova_cor,
                                                                         novo_odometro = novo_odometro,
                                                                         novo_avariado = novo_avariado,
                                                                         novo_status = novo_status)
        if veiculo_atualizado:
            st.success('Veículo atualizado')
            st.cache_data.clear()
            st.rerun()
        else:
            st.error('Erro ao atualizar o veículo')
if st.button('Atualizar Veículo'):
    atualizar_veiculo()
@st.cache_data
def carregar_dataframe():
    return ControllerVeiculo.carregar_dataframe_veiculos()

dataframe_veiculo = carregar_dataframe()
linha_selecionada = st.data_editor(dataframe_veiculo, use_container_width=True, hide_index=True)