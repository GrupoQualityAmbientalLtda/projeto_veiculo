import streamlit as st
from datetime import datetime
from PIL import Image

from src.controller.controller_formulario import ControllerFormulario
from src.controller.controller_veiculo import ControllerVeiculo
from src.controller.controller_avaria import ControllerAvaria
from src.controller.controller_registros import ControllerRegistro
from src.controller.controller_usuario import ControllerUsuario

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

# IDs temporários - ajuste conforme necessário
id_revisao = 1
id_usuario = ControllerUsuario.obter_usuario_pelo_login(st.user.email).id

st.image("imgs/logo.png")
st.header("Controle de Veículos", divider=True)

tipo = st.selectbox("Selecione o tipo:", ["Entrada", "Saída"])


with st.form("formulario_veiculo"):
    placas = ControllerVeiculo.listar_placas()
    placa_selecionada = st.selectbox("Placa do Veículo", placas)
    id_veiculo = ControllerVeiculo.obter_veiculo_por_placa(placa_selecionada)
    odometro = ControllerVeiculo.obter_odometro_veiculo(id_veiculo)
    quilometragem = st.number_input("Quilometragem", min_value=0, value=odometro)
    data = st.date_input("Data", value='today', format="DD/MM/YYYY")
    horario = st.time_input("Horário:")
    data_revisao = st.date_input("Última Revisão:", format="DD/MM/YYYY")
    destino = 'Garagem Quality'
    opcoes = list(nomes_avarias.keys())
    
    if tipo == 'Saída':
        destino = st.text_input("Selecione o destino:")
    # Checkboxes de avarias
        for i in range(0, len(opcoes), 3):
            col1, col2, col3 = st.columns(3)
            with col1:
                if i < len(opcoes):
                    st.checkbox(opcoes[i], key=f'checkbox_{i}')
            with col2:
                if i + 1 < len(opcoes):
                    st.checkbox(opcoes[i + 1], key=f'checkbox_{i + 1}')
            with col3:
                if i + 2 < len(opcoes):
                    st.checkbox(opcoes[i + 2], key=f'checkbox_{i + 2}')

        uploaded_file = st.file_uploader("Em caso de Avaria, insira uma imagem.", type=["png", "jpg", "jpeg"])

    observacoes = st.text_area("Alguma observação?")
    if st.form_submit_button("Enviar"):
        data_envio = datetime.combine(data, horario)

        # Cria formulário
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

        st.cache_data.clear()

        if isinstance(id_formulario, str):
            st.error(f"Erro ao enviar: {id_formulario}")
        elif id_formulario:
            # Coleta checkboxes
            avarias_data = {
                nomes_avarias[nome_visual]: st.session_state.get(f'checkbox_{i}', False)
                for i, nome_visual in enumerate(opcoes)
            }

            # Cria avaria e retorna id
            id_avaria = ControllerAvaria.criar_avaria(id_formulario=id_formulario, **avarias_data)

            # Salva imagem (se houver)
            if tipo == 'Saída':
                if uploaded_file:
                    try:
                        ControllerRegistro.processar_e_salvar_imagem(uploaded_file, id_avaria, id_formulario)
                        st.success("Imagem salva com sucesso!")
                    except ValueError as e:
                        st.warning(str(e))
                    except Exception as e:
                        st.error(f"Erro ao salvar imagem: {e}")
            st.success("Formulário enviado com sucesso.")
        else:
            st.error("Erro inesperado ao salvar o formulário.")
