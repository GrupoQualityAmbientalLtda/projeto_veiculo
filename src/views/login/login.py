import streamlit as st

with st.form('Login'):
    login = st.text_input('Login', placeholder="Digite seu login")
    senha = st.text_input('Senha', type="password", placeholder="Digite sua senha")
    
    fazer_login = st.form_submit_button("Fazer Login")
    
    if fazer_login:
        st.write("Login Feito")

    
