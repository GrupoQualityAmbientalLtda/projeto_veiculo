import streamlit as st

with st.form("Formulário de veículos"):
    st.header("Controle de Veículos", divider=True)
    
    data = st.date_input(label="Data",value='today',format="DD/MM/YYYY")
    
    placa = st.text_input(label="Placa do Veículo") # Possível Trocar por selectbox, encontrar forma de puxar informações do banco de dados e transformar em opções para seleção.
    # https://discuss.streamlit.io/t/can-i-add-to-a-selectbox-an-other-option-where-the-user-can-add-his-own-answer/28525/6
    tipo = st.selectbox("Selecione o tipo:",("Entrada","Saída")) # Será Selectbox
    
    pergunta = st.text_input(label="Pergunta")
    resposta = st.text_input(label="Resposta")
    data_revisao = st.date_input(label="Última Revisão:",format="DD/MM/YYYY")

    # Necessário um IF para caso seja encontrado no banco de dados como True, a opção seja travada. (Pelo menos é o que faz sentido pra mim)
    status_revisao = st.radio("Alguma avaria encontrada?", ["Sim", "Não"], captions=["Avaria encontrada em registro recente.", "Sem avarias."])

    observacoes = st.text_area("Alguma observação?")

    st.form_submit_button('Enviar Formulário')