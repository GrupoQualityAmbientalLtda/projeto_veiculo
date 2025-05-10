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
def atualizar_veiculo(dados_veiculo):
    id = st.number_input('ID', value=dados_veiculo['id'], min_value=0, disabled=True)    
    nova_placa = st.text_input('Nova Placa',value=dados_veiculo['placa'])
    novo_modelo = st.text_input('Novo Modelo', value=dados_veiculo['modelo'])
    nova_cor = st.text_input('Nova Cor', value=dados_veiculo['cor'])
    novo_odometro = st.number_input(label="Quilometragem Inicial",value=dados_veiculo['odometro'],min_value=0)
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
        if veiculo_atualizado == True:
            st.success('Veículo atualizado')
            st.cache_data.clear()
            st.rerun()
        else:
            st.error(f"Erro ao atualizar o usuário: {veiculo_atualizado}")
#if st.button('Atualizar Veículo'):
    #atualizar_veiculo()
@st.cache_data
def carregar_dataframe():
    return ControllerVeiculo.carregar_dataframe_veiculos()

dataframe_veiculo = carregar_dataframe()
linha_selecionada = st.data_editor(dataframe_veiculo, use_container_width=True, hide_index=True)

selecao = linha_selecionada[linha_selecionada['Seleção'] == True]

if len(selecao) == 1:
    dados_veiculo = {
        'id': selecao.iloc[0, 1],
        'placa': selecao.iloc[0, 2],
        'modelo': selecao.iloc[0,3],
        'cor': selecao.iloc[0,4],
        'odometro': selecao.iloc[0,5],
        'avariado': selecao.iloc[0,6],
        'status': selecao.iloc[0,7]
    }

if st.button("Atualizar Veículo") and len(selecao) == 1:
    atualizar_veiculo(dados_veiculo)