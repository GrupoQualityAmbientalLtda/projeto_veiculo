from src.models.formulario import Formulario
from src.dao.dao_formulario import DaoFormulario
from src.database.db import create_session

class ControllerFormulario:
    @classmethod
    def validar_campos_formulario(cls, id_veiculo,tipo,id_revisao,data,destino,horario,km_inicial):
        if not id_veiculo:
            return "Placa do Veículo não pode estar vazia!"
        if not tipo:
            return "Tipo não pode estar vazio!"
        if not id_revisao:
            return "Data da última revisão não pode estar vazia!"
        if not data:
            return "Data do envio não pode estar vazia!"
        if not destino:
            return "Destino não pode estar vazio!"
        if not horario:
            return "Horário não pode estar vazio!"
        if not km_inicial:
            return "Quilometragem não pode estar vazia!"
        return True
    
    @classmethod
    def criar_formulario(cls, id_veiculo,km_inicial,tipo,id_revisao,data,destino,horario):
        formulario_validado = cls.validar_campos_formulario(id_veiculo,km_inicial, tipo,id_revisao,data,destino,horario,)
        if formulario_validado != True:
            return formulario_validado

        with create_session() as session:
            try:
                criar_formulario = DaoFormulario.criar_formulario(session,id_veiculo,km_inicial,tipo,id_revisao,data,destino,horario,)
                session.commit()
                return True
            except Exception as e:
                session.rollback()
                print(f'Erro inesperado: {e}')
                return False
        
    @classmethod
    def obter_formularios_por_id(cls, id):
        with create_session() as session:
            try:
                formulario = DaoFormulario.obter_formulario_por_id(cls, session, id)
            except Exception as e:
                print(f'Erro inesperado: {e}')

    

        