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

@st.cache_data
def carregar_dataframe():
    return ControllerUsuario.carregar_dataframe_usuarios()

dataframe_usuario = carregar_dataframe()
linha_selecionada = st.data_editor(dataframe_usuario, use_container_width=True, hide_index=True)

selecao = linha_selecionada[linha_selecionada['Seleção'] == True]

if len(selecao) == 1:
    dados = {
        'id': selecao.iloc[0, 1],
        'login': selecao.iloc[0, 2],
        'nome': selecao.iloc[0,3],
        'senha': selecao.iloc[0,4],
        'permissao': selecao.iloc[0,5],
        'status': selecao.iloc[0,6]
    }
    st.text(dados)
if st.button("Atualizar Usuário"):
    atualizar_usuario()
