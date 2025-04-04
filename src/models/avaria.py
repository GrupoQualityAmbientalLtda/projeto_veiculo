from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.database.db import Base

class Avaria(Base):

    # Transformar em ENUM talvez?
    
    __tablename__ ="avarias"

    id = Column(Integer, primary_key=True)

    agua_para_brisa = Column(Boolean, nullable=False, default=False)
    adesivos = Column(Boolean, nullable=False, default=False)
    alto_falante_saida_de_som = Column(Boolean, nullable=False, default=False)
    arranhados = Column(Boolean, nullable=False, default=False)
    bancos_encostos_assentos = Column(Boolean, nullable=False, default=False)
    buzina = Column(Boolean, nullable=False, default=False)
    chave_de_roda = Column(Boolean, nullable=False, default=False)
    cintos_de_seguranca = Column(Boolean, nullable=False, default=False)
    documentos_de_carro = Column(Boolean, nullable=False, default=False)
    farol_alto = Column(Boolean, nullable=False, default=False)
    farol_baixo = Column(Boolean, nullable=False, default=False)
    fechamento_das_janelas = Column(Boolean, nullable=False, default=False)
    lanternas_frente_e_traseira = Column(Boolean, nullable=False, default=False)
    lataria_amassados = Column(Boolean, nullable=False, default=False)
    limpador_para_brisa = Column(Boolean, nullable=False, default=False)
    limpador_para_brisa_traseiro = Column(Boolean, nullable=False, default=False)
    luz_da_placa_licenca = Column(Boolean, nullable=False, default=False)
    luz_de_freio = Column(Boolean, nullable=False, default=False)
    luz_de_re = Column(Boolean, nullable=False, default=False)
    luz_interna = Column(Boolean, nullable=False, default=False)
    luzes_painel = Column(Boolean, nullable=False, default=False)
    macaco = Column(Boolean, nullable=False, default=False)
    nivel_da_agua_radiador = Column(Boolean, nullable=False, default=False)
    oleo_do_freio = Column(Boolean, nullable=False, default=False)
    oleo_do_motor = Column(Boolean, nullable=False, default=False)
    para_brisa = Column(Boolean, nullable=False, default=False)
    para_choque_dianteiro = Column(Boolean, nullable=False, default=False)
    para_choque_traseiro = Column(Boolean, nullable=False, default=False)
    pisca_alerta = Column(Boolean, nullable=False, default=False)
    pneu_estado_assentos = Column(Boolean, nullable=False, default=False)
    pneu_reserva_estepe = Column(Boolean, nullable=False, default=False)
    portas_travas = Column(Boolean, nullable=False, default=False)
    quebra_sol = Column(Boolean, nullable=False, default=False)
    retrovisores_externos = Column(Boolean, nullable=False, default=False)
    retrovisores_internos = Column(Boolean, nullable=False, default=False)
    seta_direita_e_esquerda = Column(Boolean, nullable=False, default=False)
    tapete = Column(Boolean, nullable=False, default=False)
    triangulo_de_sinalizacao = Column(Boolean, nullable=False, default=False)
    velocimetro_tacografo = Column(Boolean, nullable=False, default=False)