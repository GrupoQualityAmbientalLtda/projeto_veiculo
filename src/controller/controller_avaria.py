from src.dao.dao_avaria import DaoAvaria
from src.dao.dao_veiculo import DaoVeiculo
from src.dao.dao_formulario import DaoFormulario
from src.utils.simple_mail import send_mail_zepto
from src.database.db import create_session
import pandas as pd
class ControllerAvaria:
    @classmethod
    def criar_avaria(cls, id_formulario: int, **kwargs):
        """
        Cria uma avaria no banco associada a um formulário.
        """
        with create_session() as session:
            avaria_id = DaoAvaria.criar_avaria(session, id_formulario=id_formulario, **kwargs)
            formulario = DaoFormulario.obter_formulario_por_id(session, id_formulario)
            if any(kwargs.values()):
                DaoVeiculo.atualizar_avariado_veiculo(session, formulario.id_veiculo, True)
                corpo = "Segue a relação das avarias:\n"
                avarias = cls.listar_avarias_verdadeiras()
                for avaria_dict in avarias:
                    for nome, valor in avaria_dict.items():
                        if nome not in ("ID", "ID Formulário") and valor:
                            corpo += f"- {nome}\n"

                send_mail_zepto(corpo)
                session.commit()
            else:
                DaoVeiculo.atualizar_avariado_veiculo(session, formulario.id_veiculo, False)
                session.commit()
            return avaria_id
        
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

    @classmethod
    def carregar_dataframe_avarias(cls):
        with create_session() as session:
            avarias = DaoAvaria.listar_avarias(session)

            dataframe_avarias = pd.DataFrame([
                {
                    "ID": avaria.id,
                    "ID Formulário": avaria.id_formulario,
                    **{
                        nome_legivel: getattr(avaria, nome_interno)
                        for nome_legivel, nome_interno in cls.nomes_avarias.items()
                    }
                }
                for avaria in avarias
            ])

            dataframe_avarias['Seleção'] = False
            colunas_ordenadas = ['Seleção', 'ID', 'ID Formulário'] + list(cls.nomes_avarias.keys())
            dataframe_avarias = dataframe_avarias.reindex(columns=colunas_ordenadas)

            return dataframe_avarias
    
    @classmethod
    def listar_avarias_verdadeiras(cls):
        with create_session() as session:
            avaria = DaoAvaria.listar_ultima_avaria(session)
            resultado = []

            if avaria:
                avarias_verdadeiras = {
                    nome_legivel: True
                    for nome_legivel, nome_interno in cls.nomes_avarias.items()
                    if getattr(avaria, nome_interno)
                } 
                if avarias_verdadeiras:
                    resultado.append({
                        "ID": avaria.id,
                        "ID Formulário": avaria.id_formulario,
                        **avarias_verdadeiras
                })
            return resultado

    # FUNÇÃO EXIBIR TODAS AVARIAS    
    # @classmethod
    # def listar_avarias_verdadeiras(cls):
    #     with create_session() as session:
    #         avarias = DaoAvaria.listar_avarias(session)
    #         resultado = []

    #         for avaria in avarias:
    #             avarias_verdadeiras = {
    #                 nome_legivel: True
    #                 for nome_legivel, nome_interno in cls.nomes_avarias.items()
    #                 if getattr(avaria, nome_interno)
    #             } 
    #             if avarias_verdadeiras:
    #                 resultado.append({
    #                     "ID": avaria.id,
    #                     "ID Formulário": avaria.id_formulario,
    #                     **avarias_verdadeiras
    #             })
    #         return resultado
