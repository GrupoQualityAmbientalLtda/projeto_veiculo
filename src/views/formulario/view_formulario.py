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
from src.controller.controller_avaria import ControllerAvaria

from datetime import datetime

nomes_avarias = {
    'Água Para-Brisa': 'agua_para_brisa',
    'Adesivos': 'adesivos',
    'Alto Falante (Saída de Som)': 'alto_falante_saida_de_som',
    'Arranhados': 'arranhados',
    'Bancos (Encostos/Assentos)': 'bancos_encostos_assentos',
    'Buzina': 'buzina',
    'Chave de Roda': 'chave_de_roda',
    'Cintos de Segurança': 'cintos_de_seguranca',
    'Documentos de Carro': 'documentos_de_carro',
    'Farol Alto': 'farol_alto',
    'Farol Baixo': 'farol_baixo',
    'Fechamento das Janelas': 'fechamento_das_janelas',
    'Lanternas Frente e Traseira': 'lanternas_frente_e_traseira',
    'Lataria (Amassados)': 'lataria_amassados',
    'Limpador Para-Brisa': 'limpador_para_brisa',
    'Limpador Para-Brisa Traseiro': 'limpador_para_brisa_traseiro',
    'Luz da Placa (Licença)': 'luz_da_placa_licenca',
    'Luz de Freio': 'luz_de_freio',
    'Luz de Ré': 'luz_de_re',
    'Luz Interna': 'luz_interna',
    'Luzes Painel': 'luzes_painel',
    'Macaco': 'macaco',
    'Nível da Água Radiador': 'nivel_da_agua_radiador',
    'Óleo do Freio': 'oleo_do_freio',
    'Óleo do Motor': 'oleo_do_motor',
    'Para Brisa': 'para_brisa',
    'Para-Choque Dianteiro': 'para_choque_dianteiro',
    'Para-Choque Traseiro': 'para_choque_traseiro',
    'Pisca Alerta': 'pisca_alerta',
    'Pneu (Estado/Assentos)': 'pneu_estado_assentos',
    'Pneu Reserva (Estepe)': 'pneu_reserva_estepe',
    'Portas/Travas': 'portas_travas',
    'Quebra Sol': 'quebra_sol',
    'Retrovisores Externos': 'retrovisores_externos',
    'Retrovisores Internos': 'retrovisores_internos',
    'Seta Direita e Esquerda': 'seta_direita_e_esquerda',
    'Tapete': 'tapete',
    'Triângulo de Sinalização': 'triangulo_de_sinalizacao',
    'Velocímetro/Tacógrafo': 'velocimetro_tacografo'
}


with st.form("Formulário de veículos"):
    id_veiculo = 1
    id_revisao = 1
    id_usuario = 1
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
    
    opcoes = list(nomes_avarias.keys())


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

    

        # if isinstance(resultado, str):  # Se retornou mensagem de erro
        #     st.error(f"Erro ao enviar: {resultado}")
        #     print(f"Resultado retornado: {resultado} ({type(resultado)})")

        # elif resultado:
        #     st.success("Formulário e destino salvos com sucesso.")
        # else:
        #     st.error("Erro inesperado ao salvar o formulário.")

    if st.form_submit_button("Enviar"):
    # IDS TEMPORARIOS
        id_veiculo = 1
        id_revisao = 1
        id_usuario = 1

        data_envio = datetime.combine(data, horario)

        id_formulario = ControllerFormulario.criar_formulario(
            id_usuario=id_usuario,
            id_veiculo=id_veiculo,
            quilometragem=quilometragem,
            tipo=tipo,
            id_revisao=id_revisao,
            data=data_envio,
            destino=destino,
            observacao=observacoes
        )

        if isinstance(id_formulario, str):
            st.error(f"Erro ao enviar: {id_formulario}")
        elif id_formulario:
            # Obter valores das checkboxes
            avarias_data = {}
            for i, nome_visual in enumerate(opcoes):
                nome_model = nomes_avarias[nome_visual]
                avarias_data[nome_model] = st.session_state.get(f'checkbox_{i}', False)

            ControllerAvaria.criar_avaria(id_formulario=id_formulario, **avarias_data)
            st.success("Formulário e checklist de avarias enviados com sucesso.")
        else:
            st.error("Erro inesperado ao salvar o formulário.")


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
