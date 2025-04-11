from src.models.veiculo import Veiculo

class DaoVeiculo:
    @classmethod
    def criar_veiculo(cls, session, placa, modelo, cor, odometro, avariado):
        veiculo = Veiculo(placa = placa, modelo = modelo, cor = cor, odometro = odometro, avariado = avariado)
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
    