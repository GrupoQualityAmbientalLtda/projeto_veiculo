from src.models.avaria import Avaria


class DaoAvaria:
    @classmethod
    # CRIAR FK PARA ESTA TABELA // 
    def criar_avaria(
        cls,
        session,
        agua_para_brisa=False,
        adesivos=False,
        alto_falante_saida_de_som=False,
        arranhados=False,
        bancos_encostos_assentos=False,
        buzina=False,
        chave_de_roda=False,
        cintos_de_seguranca=False,
        documentos_de_carro=False,
        farol_alto=False,
        farol_baixo=False,
        fechamento_das_janelas=False,
        lanternas_frente_e_traseira=False,
        lataria_amassados=False,
        limpador_para_brisa=False,
        limpador_para_brisa_traseiro=False,
        luz_da_placa_licenca=False,
        luz_de_freio=False,
        luz_de_re=False,
        luz_interna=False,
        luzes_painel=False,
        macaco=False,
        nivel_da_agua_radiador=False,
        oleo_do_freio=False,
        oleo_do_motor=False,
        para_brisa=False,
        para_choque_dianteiro=False,
        para_choque_traseiro=False,
        pisca_alerta=False,
        pneu_estado_assentos=False,
        pneu_reserva_estepe=False,
        portas_travas=False,
        quebra_sol=False,
        retrovisores_externos=False,
        retrovisores_internos=False,
        seta_direita_e_esquerda=False,
        tapete=False,
        triangulo_de_sinalizacao=False,
        velocimetro_tacografo=False,
    ):
        """
        Essa função faz a criação das avarias no banco de dados, recebendo True ou False como seus valores em tipo Boolean.

        Seus parâmetros são, as avarias citadas.
        """
        avaria = Avaria(
            agua_para_brisa=agua_para_brisa,
            adesivos=adesivos,
            alto_falante_saida_de_som=alto_falante_saida_de_som,
            arranhados=arranhados,
            bancos_encostos_assentos=bancos_encostos_assentos,
            buzina=buzina,
            chave_de_roda=chave_de_roda,
            cintos_de_seguranca=cintos_de_seguranca,
            documentos_de_carro=documentos_de_carro,
            farol_alto=farol_alto,
            farol_baixo=farol_baixo,
            fechamento_das_janelas=fechamento_das_janelas,
            lanternas_frente_e_traseira=lanternas_frente_e_traseira,
            lataria_amassados=lataria_amassados,
            limpador_para_brisa=limpador_para_brisa,
            limpador_para_brisa_traseiro=limpador_para_brisa_traseiro,
            luz_da_placa_licenca=luz_da_placa_licenca,
            luz_de_freio=luz_de_freio,
            luz_de_re=luz_de_re,
            luz_interna=luz_interna,
            luzes_painel=luzes_painel,
            macaco=macaco,
            nivel_da_agua_radiador=nivel_da_agua_radiador,
            oleo_do_freio=oleo_do_freio,
            oleo_do_motor=oleo_do_motor,
            para_brisa=para_brisa,
            para_choque_dianteiro=para_choque_dianteiro,
            para_choque_traseiro=para_choque_traseiro,
            pisca_alerta=pisca_alerta,
            pneu_estado_assentos=pneu_estado_assentos,
            pneu_reserva_estepe=pneu_reserva_estepe,
            portas_travas=portas_travas,
            quebra_sol=quebra_sol,
            retrovisores_externos=retrovisores_externos,
            retrovisores_internos=retrovisores_internos,
            seta_direita_e_esquerda=seta_direita_e_esquerda,
            tapete=tapete,
            triangulo_de_sinalizacao=triangulo_de_sinalizacao,
            velocimetro_tacografo=velocimetro_tacografo,
        )

        session.add(avaria)
        session.commit()
        return avaria
    @classmethod
    def obter_avaria(cls, session, id):
        avaria = session.query(Avaria).filter(Avaria.id == id).first()
        return avaria
