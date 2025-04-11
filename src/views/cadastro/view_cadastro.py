import streamlit as st

with st.form('Cadastro'):
    st.image("imgs/logo.png")
    nome = st.text_input('Nome',placeholder="Digite seu nome")
    login = st.text_input('Usuário', placeholder="Digite seu usuário")
    senha = st.text_input('Senha', type="password", placeholder="Digite sua senha")
    confirmar_senha = st.text_input('Confirmar senha', type="password", placeholder="Confirme sua senha")
    permissao = st.selectbox("Permissão:",('Gestor','Motorista'),)
    status = st.selectbox('Status:',('Ativo','Inativo'))
    
    fazer_cadastro = st.form_submit_button("Fazer Cadastro")
    
    if fazer_cadastro:
        st.write("Cadastro Feito")

    
