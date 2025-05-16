from src.models.veiculo import Veiculo


class DaoVeiculo:    
    @classmethod
    def criar_veiculo(cls, session, placa, modelo, cor, odometro, avariado, status):
        veiculo = Veiculo(placa = placa, modelo = modelo, cor = cor, odometro = odometro, avariado = avariado, status = status)
        session.add(veiculo)
        session.commit()
        return veiculo
    
    @classmethod
    def obter_veiculo_por_id(cls, session, id):
        veiculo = session.query(Veiculo).filter(Veiculo.id == id).first()
        return veiculo
    
    @classmethod
    def obter_veiculo_por_placa(cls, session, placa):
        veiculo = session.query(Veiculo).filter(Veiculo.placa == placa).first()
        return veiculo
    
    @classmethod
    def listar_todos_veiculos(cls, session):
        return session.query(Veiculo).all()
    
    @classmethod
    def deletar_veiculo(cls, session, id):
        veiculo = session.query(Veiculo).filter(Veiculo.id == id).first()
        if veiculo:
            session.delete(veiculo)
            session.commit()
            return True
        return False
    @classmethod
    def atualizar_veiculo_pelo_id(cls, session, id, nova_placa, novo_modelo, nova_cor, novo_odometro, novo_avariado, novo_status):
        veiculo = session.query(Veiculo).filter(Veiculo.id == id).first()
        if veiculo is None:
            raise ValueError(f"Veículo com ID {id} não encontrado.")  # Dispara erro se não encontrar
        
        veiculo.placa = nova_placa
        veiculo.modelo = novo_modelo
        veiculo.cor = nova_cor
        veiculo.odometro = novo_odometro
        veiculo.avariado = novo_avariado
        veiculo.status = novo_status
        
        session.add(veiculo)  # Atualiza o objeto na sessão
        return veiculo
    
    @classmethod
    def atualizar_odometro_veiculo(cls, session, id, novo_odometro):
        veiculo = session.query(Veiculo).filter(Veiculo.id == id).first() # Ou veiculo.odometro
        veiculo.odometro = novo_odometro
        return veiculo

# UPDATE ODOMETRO
            