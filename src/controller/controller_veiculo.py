from src.database.db import create_session
from src.dao.dao_veiculo import DaoVeiculo
from src.models.veiculo import Veiculo
import pandas as pd

class ControllerVeiculo:
    @classmethod
    def validar_campos_veiculo(cls, placa, modelo, cor, odometro, avariado, status):
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
        if status is None:
            return "Informe se o veículo está ou não ativo."
        return True

    @classmethod
    def obter_odometro_veiculo(cls, id):
        with create_session() as session:
            veiculo = DaoVeiculo.obter_veiculo_por_id(session, id)
            odometro = veiculo.odometro
            return odometro

    @classmethod
    def listar_placas(cls):
        with create_session() as session:
            veiculos = DaoVeiculo.listar_todos_veiculos(session)
            return [veiculo.placa for veiculo in veiculos]
    @classmethod
    def obter_id_veiculo_por_placa(cls, placa):
        with create_session() as session:
            veiculo = DaoVeiculo.obter_veiculo_por_placa(session, placa)
            return veiculo.id
        
    @classmethod
    def obter_estado_pela_placa(cls, placa):
        with create_session() as session:
            veiculo = DaoVeiculo.obter_veiculo_por_placa(session, placa)
            return veiculo.avariado
        
    @classmethod
    def criar_veiculo(cls, placa, modelo, cor, odometro, avariado, status):
        campos_validados = cls.validar_campos_veiculo(placa, modelo, cor, odometro, avariado, status)
        if campos_validados != True:
            return campos_validados
        with create_session() as session:
            try:
                # Agora passando a session corretamente
                veiculo = DaoVeiculo.criar_veiculo(session, placa, modelo, cor, odometro, avariado, status)
                return veiculo
            except Exception as e:
                print(f'Erro inesperado: {e}')
                session.rollback()
                return False
        
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
    def atualizar_veiculo_pelo_id(cls, id, nova_placa, novo_modelo, nova_cor, novo_odometro, novo_avariado, novo_status):
        with create_session() as session:
            try:
                DaoVeiculo.atualizar_veiculo_pelo_id(session, id, nova_placa, novo_modelo, nova_cor, novo_odometro, novo_avariado, novo_status)
                session.commit()
                return True
            except Exception as e:
                print(f'Erro gerado {e}')
                session.rollback()
                return None
            
    @classmethod
    def carregar_dataframe_veiculos(cls):
        with create_session() as session:
            veiculos = DaoVeiculo.listar_todos_veiculos(session)

            dataframe_veiculo = pd.DataFrame([
                {
                    "ID": veiculo.id,
                    "Placa": veiculo.placa,
                    "Modelo": veiculo.modelo,
                    "Cor": veiculo.cor,
                    "Odometro": veiculo.odometro,
                    "Avariado": "Sim" if veiculo.avariado else "Não",
                    "Status": veiculo.status.value if veiculo.status else None
                }
                for veiculo in veiculos
            ])
            dataframe_veiculo['Seleção'] = False
            dataframe_veiculo = dataframe_veiculo.reindex(columns=['Seleção', 'ID', 'Placa', 'Modelo', 'Cor', 'Odometro', 'Avariado', 'Status'])
            return dataframe_veiculo
