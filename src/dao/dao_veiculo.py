from src.models.veiculo import Veiculo

class DaoVeiculo:
    @classmethod
    def criar_veiculo(cls, session, placa, modelo, cor, odometro, avariado, status):
        veiculo = Veiculo(placa = placa, modelo = modelo, cor = cor, odometro = odometro, avariado = avariado, status = status)
        session.add(veiculo)
        session.commit()
        return veiculo
    
    @classmethod
    def obter_veiculo(cls, session, id):
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
            