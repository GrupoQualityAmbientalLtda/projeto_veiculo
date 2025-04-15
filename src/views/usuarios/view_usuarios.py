import streamlit as st
from src.controller.controller_usuario import ControllerUsuario
import pandas as pd
# Status e Permissao
from src.models.usuario import Status, PermissaoEnum
from src.database.db import create_session

session = create_session()

st.title("Consulta de Usuários")
st.subheader("Pesquisa:")

@st.dialog(title='Criar Usuário')
def criar_usuario():
    nome = st.text_input('Nome')
    login = st.text_input('Login')
    senha = st.text_input('Senha', type='password')
    lista_status = [status.value for status in Status]
    status = st.selectbox('Status', lista_status)
    lista_permissao = [permissao.value for permissao in PermissaoEnum]
    permissao = st.selectbox('Permissao', lista_permissao)
    botao_cadastrar = st.button('Cadastrar Cliente', key='botao_cadastrar_usuario')
    if botao_cadastrar:
        usuario_salvo = ControllerUsuario.cadastrar_usuario(nome = nome , 
                                                            login = login, 
                                                            senha = senha, 
                                                            permissao = permissao, 
                                                            status = status)
        if usuario_salvo:
            st.success('Usuário Cadastrado com Sucesso!')
            st.cache_data.clear()
            st.rerun()
        else:
            st.error('Erro ao cadastrar o usuário!')

if st.button("Novo Usuário"):
    criar_usuario()

@st.dialog(title='Editar Usuário')
def atualizar_usuario():
    id = st.number_input('ID',value=0,min_value=0)
    novo_nome = st.text_input('Novo Nome')
    novo_login = st.text_input('Novo Login')
    nova_senha = st.text_input('Nova Senha', type='password')
    lista_status = [status.value for status in Status]
    novo_status = st.selectbox('Novo Status', lista_status)
    lista_permissao = [permissao.value for permissao in PermissaoEnum]
    nova_permissao = st.selectbox('Nova Permissão', lista_permissao)
    botao_atualizar = st.button('Atualizar Usuário', key='botao_atualizar_usuario')

    if botao_atualizar:
        usuario_atualizado = ControllerUsuario.atualizar_usuario_pelo_id(id = id,
                                                                         novo_nome = novo_nome, 
                                                                         novo_login = novo_login,
                                                                         nova_senha = nova_senha, 
                                                                         nova_permissao = nova_permissao, 
                                                                         novo_status = novo_status)
        if usuario_atualizado:
            st.success('Usuário Atualizado com Sucesso!')
            st.cache_data.clear()
            st.rerun()
        else:
            st.error('Erro ao atualizar o usuário')
if st.button("Atualizar Usuário"):
    atualizar_usuario()

@st.cache_data
def carregar_dataframe():
    return ControllerUsuario.carregar_dataframe_usuarios()

dataframe_veiculo = carregar_dataframe()
linha_selecionada = st.data_editor(dataframe_veiculo, use_container_width=True)


