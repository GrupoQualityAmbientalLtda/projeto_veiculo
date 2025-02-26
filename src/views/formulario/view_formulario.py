import streamlit as st

with st.form("Formulário de veículos"):
    st.header("Controle de Veículos", divider=True)
    st.image("imgs/logo.png")
    
    data = st.date_input(label="Data",value='today',format="DD/MM/YYYY")
    
    placa = st.text_input(label="Placa do Veículo") # Possível Trocar por selectbox, encontrar forma de puxar informações do banco de dados e transformar em opções para seleção.
    # https://discuss.streamlit.io/t/can-i-add-to-a-selectbox-an-other-option-where-the-user-can-add-his-own-answer/28525/6
    
    quilometragem = st.number_input(label="Quilometragem Inicial",value=0,min_value=0)

    tipo = st.selectbox("Selecione o tipo:",("Entrada","Saída")) # Será Selectbox
    
    horario = st.time_input("Horário:")
    
    data_revisao = st.date_input(label="Última Revisão:",format="DD/MM/YYYY")

    # Necessário um IF para caso seja encontrado no banco de dados como True, a opção seja travada. (Pelo menos é o que faz sentido pra mim)
    #status_revisao = st.radio("Alguma avaria encontrada?", ["Sim", "Não"], captions=["Avaria encontrada em registro recente.", "Sem avarias."])

    opcoes = [
    'Água Para-Brisa',
    'Adesivos',
    'Alto Falante (Saída de Som)',
    'Arranhados',
    'Bancos (Encostos/Assentos)',
    'Buzina',
    'Chave de Roda',
    'Cintos de Segurança',
    'Documentos de Carro',
    'Farol Alto',
    'Farol Baixo',
    'Fechamento das Janelas',
    'Lanternas Frente e Traseira',
    'Lataria (Amassados)',
    'Limpador Para-Brisa',
    'Limpador Para-Brisa Traseiro',
    'Luz da Placa (Licença)',
    'Luz de Freio',
    'Luz de Ré',
    'Luz Interna',
    'Luzes Painel',
    'Macaco',
    'Nível da Água Radiador',
    'Óleo do Freio',
    'Óleo do Motor',
    'Para Brisa',
    'Para-Choque Dianteiro',
    'Para-Choque Traseiro',
    'Pisca Alerta',
    'Pneu (Estado/Assentos)',
    'Pneu Reserva (Estepe)',
    'Portas/Travas',
    'Quebra Sol',
    'Retrovisores Externos',
    'Retrovisores Internos',
    'Seta Direita e Esquerda',
    'Tapete',
    'Triângulo de Sinalização',
    'Velocímetro/Tacógrafo'
]
    # Dividir as opções em grupos de 3
    for i in range(0, len(opcoes), 3):
        col1, col2, col3 = st.columns(3)  # Cria 3 colunas
        with col1:
            if i < len(opcoes):
                st.checkbox(opcoes[i], key=f'checkbox_{i}')
        with col2:
            if i + 1 < len(opcoes):
                st.checkbox(opcoes[i + 1], key=f'checkbox_{i + 1}')
        with col3:
            if i + 2 < len(opcoes):
                st.checkbox(opcoes[i + 2], key=f'checkbox_{i + 2}')

    observacoes = st.text_area("Alguma observação?")

    # INSERIR RUBRICA

    st.form_submit_button('Enviar Formulário')