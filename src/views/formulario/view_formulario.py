import streamlit as st
from PIL import Image
import io
from src.controller.controller_registros import processar_e_salvar_imagem
from src.models.registros import Registro
from src.dao.dao_registro import salvar_registro
from src.database.db import create_session
from src.dao.dao_destinos import DaoDestino
from src.dao.dao_formulario import DaoFormulario
from src.controller.controller_formulario import ControllerFormulario
from src.controller.controller_veiculo import ControllerVeiculo

from datetime import datetime

with st.form("Formulário de veículos"):
    
    st.image("imgs/logo.png")
    st.header("Controle de Veículos", divider=True)
    
    
    placas = ControllerVeiculo.listar_placas()
    placa_selecionada = st.selectbox("Placa do Veículo", placas)
    
    quilometragem = st.number_input(label="Quilometragem Inicial",value=0,min_value=0)

    tipo = st.selectbox("Selecione o tipo:",("Entrada","Saída")) # Será Selectbox
    
    data = st.date_input(label="Data",value='today',format="DD/MM/YYYY")
    horario = st.time_input("Horário:")
    
    data_revisao = st.date_input(label="Última Revisão:",format="DD/MM/YYYY")
    observacoes = st.text_area("Alguma observação?")

    destino = st.text_input("Selecione o destino:")
    if st.form_submit_button("Enviar"):
        # IDS TEMPORARIOS
        id_veiculo = 1
        id_revisao = 1
        id_usuario = 1

        # JUNTAR DATA DE ENVIO + HORARIO E SALVAR NO BANCO
        data_envio = datetime.combine(data, horario)

        resultado = ControllerFormulario.criar_formulario(
            id_usuario = id_usuario,
            id_veiculo=id_veiculo,
            quilometragem=quilometragem,
            tipo=tipo,
            id_revisao=id_revisao,
            data=data_envio,
            destino=destino,
            observacao=observacoes
        )

        if isinstance(resultado, str):  # Se retornou mensagem de erro
            st.error(f"Erro ao enviar: {resultado}")
            print(f"Resultado retornado: {resultado} ({type(resultado)})")

        elif resultado:
            st.success("Formulário e destino salvos com sucesso.")
        else:
            st.error("Erro inesperado ao salvar o formulário.")

#     opcoes = [
#     'Água Para-Brisa',
#     'Adesivos',
#     'Alto Falante (Saída de Som)',
#     'Arranhados',
#     'Bancos (Encostos/Assentos)',
#     'Buzina',
#     'Chave de Roda',
#     'Cintos de Segurança',
#     'Documentos de Carro',
#     'Farol Alto',
#     'Farol Baixo',
#     'Fechamento das Janelas',
#     'Lanternas Frente e Traseira',
#     'Lataria (Amassados)',
#     'Limpador Para-Brisa',
#     'Limpador Para-Brisa Traseiro',
#     'Luz da Placa (Licença)',
#     'Luz de Freio',
#     'Luz de Ré',
#     'Luz Interna',
#     'Luzes Painel',
#     'Macaco',
#     'Nível da Água Radiador',
#     'Óleo do Freio',
#     'Óleo do Motor',
#     'Para Brisa',
#     'Para-Choque Dianteiro',
#     'Para-Choque Traseiro',
#     'Pisca Alerta',
#     'Pneu (Estado/Assentos)',
#     'Pneu Reserva (Estepe)',
#     'Portas/Travas',
#     'Quebra Sol',
#     'Retrovisores Externos',
#     'Retrovisores Internos',
#     'Seta Direita e Esquerda',
#     'Tapete',
#     'Triângulo de Sinalização',
#     'Velocímetro/Tacógrafo'
# ]
#     # Dividir as opções em grupos de 3
#     for i in range(0, len(opcoes), 3):
#         col1, col2, col3 = st.columns(3)  # Cria 3 colunas
#         with col1:
#             if i < len(opcoes):
#                 st.checkbox(opcoes[i], key=f'checkbox_{i}')
#         with col2:
#             if i + 1 < len(opcoes):
#                 st.checkbox(opcoes[i + 1], key=f'checkbox_{i + 1}')
#         with col3:
#             if i + 2 < len(opcoes):
#                 st.checkbox(opcoes[i + 2], key=f'checkbox_{i + 2}')

    

#     enviar_imagens = st.file_uploader("Insira imagens das avarias:", accept_multiple_files=True)

#     # INSERIR RUBRICA

#     # if st.form_submit_button('Enviar Formulário'):
#     #     if not placa.strip():
#     #         st.warning('Por favor, preencha todos os campos.')
#     #     else:
#     #         st.sucess('Formulário enviado com sucesso')


# with st.form("Formulário de teste"):

#     uploaded_file = st.file_uploader("Envie uma imagem", type=["png", "jpg", "jpeg"])
#     if st.form_submit_button("Enviar"):
#         try:
#             processar_e_salvar_imagem(uploaded_file)
#             st.success("Imagem salva com sucesso!")
#         except ValueError as e:
#             st.warning(str(e))
#         except Exception as e:
#             st.error(f"Erro inesperado: {e}")
