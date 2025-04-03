from src.models.veiculo import Veiculo

class DaoVeiculo:
    @classmethod
    def criar_veiculo(cls, session, placa, modelo, cor):
        veiculo = Veiculo(placa= placa, modelo = modelo, cor = cor)
        session.add(veiculo)
        session.commit()
        return veiculo
    
    @classmethod
    def obter_veiculo(cls, session, id):
        veiculo = session.query(Veiculo).filter(Veiculo.id == id).first()
        return veiculo
    