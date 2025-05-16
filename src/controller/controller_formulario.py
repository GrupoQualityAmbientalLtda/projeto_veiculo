from src.models.formulario import Formulario
from src.dao.dao_formulario import DaoFormulario
from src.database.db import create_session
from src.dao.dao_destinos import DaoDestino
from src.dao.dao_veiculo import DaoVeiculo

class ControllerFormulario:
    @classmethod
    def validar_campos_formulario(cls, id_usuario, id_veiculo,tipo,id_revisao,data,destino,quilometragem):
        if not id_usuario:
            return "Usuário não identificado!"
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
        if not quilometragem:
            return "Quilometragem não pode estar vazia!"
        return True
    
    @classmethod
    def criar_formulario(cls, id_usuario,id_veiculo, quilometragem, tipo, id_revisao, data, destino, observacao):
        validado = cls.validar_campos_formulario(id_veiculo, id_usuario,tipo, id_revisao, data, destino, quilometragem)
        if validado != True:
            return validado  # retorna string com erro

        with create_session() as session:
            try:
                formulario = DaoFormulario.criar_formulario(
                    id_usuario = id_usuario,
                    session=session,
                    id_veiculo=id_veiculo,
                    tipo=tipo,
                    id_revisao=id_revisao,
                    data=data,
                    observacao=observacao,
                    quilometragem=quilometragem,
                )
                DaoDestino.criar_destino(
                    session=session,
                    destino=destino,
                    id_formulario=formulario.id
                )

                DaoVeiculo.atualizar_odometro_veiculo(
                    session = session,
                    id = id_veiculo,
                    novo_odometro = quilometragem

                )

                

                session.commit()
                return formulario.id
            except Exception as e:
                session.rollback()
                print(f'Erro ao criar formulário: {e}')
                return False
        
    @classmethod
    def obter_formularios_por_id(cls, id):
        with create_session() as session:
            try:
                formulario = DaoFormulario.obter_formulario_por_id(session, id)
                return formulario
            except Exception as e:
                print(f'Erro inesperado: {e}')

    @classmethod
    def obter_todos_formularios(cls):
        with create_session() as session:
            try:
                formulario = DaoFormulario.obter_todos_formularios(session)
                return formulario
            except Exception as e:
                print(f'Erro inesperado {e}')

    

        