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
def atualizar_usuario(dados_usuario):
    id = st.number_input('ID', value=dados_usuario['id'], min_value=0, disabled=True)  # ID fixo
    novo_nome = st.text_input('Novo Nome', value=dados_usuario['nome'])
    novo_login = st.text_input('Novo Login', value=dados_usuario['login'])
    nova_senha = st.text_input('Nova Senha', type='password')  # Senha em branco por padrão
    lista_status = [status.value for status in Status]
    novo_status = st.selectbox('Novo Status', lista_status, index=lista_status.index(dados_usuario['status']) if dados_usuario['status'] else 0)
    lista_permissao = [permissao.value for permissao in PermissaoEnum]
    nova_permissao = st.selectbox('Nova Permissão', lista_permissao, index=lista_permissao.index(dados_usuario['permissao']) if dados_usuario['permissao'] else 0)
    botao_atualizar = st.button('Atualizar Usuário', key='botao_atualizar_usuario')

    if botao_atualizar:
        resultado = ControllerUsuario.atualizar_usuario_pelo_id(
            id=id,
            novo_nome=novo_nome,
            novo_login=novo_login,
            nova_senha=nova_senha,
            nova_permissao=nova_permissao,
            novo_status=novo_status
        )

        if resultado == True:
            st.success('Usuário Atualizado com Sucesso!')
            st.cache_data.clear()
            st.rerun()
        else:
            st.error(f"Erro ao atualizar o usuário: {resultado}")  # Exibe o erro detalhado retornado pela função


@st.cache_data
def carregar_dataframe():
    return ControllerUsuario.carregar_dataframe_usuarios()

dataframe_usuario = carregar_dataframe()
linha_selecionada = st.data_editor(dataframe_usuario, use_container_width=True, hide_index=True)

selecao = linha_selecionada[linha_selecionada['Seleção'] == True]

if len(selecao) == 1:
    dados_usuario = {
        'id': selecao.iloc[0, 1],
        'login': selecao.iloc[0, 2],
        'nome': selecao.iloc[0,3],
        'senha': selecao.iloc[0,4],
        'permissao': selecao.iloc[0,5],
        'status': selecao.iloc[0,6]
    }

if st.button("Atualizar Usuário") and len(selecao) == 1:
    atualizar_usuario(dados_usuario)
