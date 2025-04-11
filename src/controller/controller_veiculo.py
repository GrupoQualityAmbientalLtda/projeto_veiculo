from src.database.db import create_session
from src.dao.dao_veiculo import DaoVeiculo
from src.models.veiculo import Veiculo

class ControllerVeiculo:
    @classmethod
    def validar_campos_veiculo(cls, placa, modelo, cor, odometro, avariado):
        if not placa:
            return "Placa do veículo não pode estar vazia!"
        if not modelo:
            return "Modelo do veículo não pode estar vazio!"
        if not cor:
            return "Cor do veículo não pode estar vazia!"
        if odometro is None or odometro < 0:
            return "Odômetro deve ser um número válido e não pode ser negativo!"
        if avariado is None:
            return "Informe se o veículo está ou não avariado."
        return True

    @classmethod
    def listar_placas(cls):
        with create_session() as session:
            veiculos = DaoVeiculo.listar_todos_veiculos(session)
            return [veiculo.placa for veiculo in veiculos]
        
    @classmethod
    def criar_veiculo(cls, placa, modelo, cor, odometro, avariado):
        campos_validados = cls.validar_campos_veiculo(placa, modelo, cor, odometro, avariado)
        if campos_validados != True:
            return campos_validados
        with create_session() as session:
            try:
                veiculos = DaoVeiculo.criar_veiculo(placa, modelo, cor, odometro, avariado)
                return veiculos
            except Exception as e:
                print(f'Erro inesperado: {e}')
        
    @classmethod
    def deletar_veiculo(cls, id):
        with create_session() as session:
            try:
                deletar_veiculo = DaoVeiculo.deletar_veiculo(session, id)
                if deletar_veiculo:
                    return True
                else:
                    return "Veículo não encontrado!"
            except Exception as e:
                print(f"Erro ao deletar veículo: {e}")
                return False
    @classmethod
    def atualizar_veiculo_pelo_id(cls, id, nova_placa, novo_modelo, nova_cor, novo_odometro, novo_avariado):
        with create_session() as session:
            try:
                DaoVeiculo.atualizar_veiculo(session, id, nova_placa, novo_modelo, nova_cor, novo_odometro, novo_avariado)
                session.commit()
                return True
            except Exception as e:
                print(f'Erro gerado {e}')
                session.rollback()
                return None