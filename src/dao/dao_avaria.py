from src.models.avaria import Avaria


class DaoAvaria:
    @classmethod
    def criar_avaria(cls, session, id_formulario: int, **kwargs):
        """
        Cria uma instância de Avaria com base nas avarias recebidas via kwargs (booleanas).
        """
        avaria = Avaria(id_formulario=id_formulario, **kwargs)
        session.add(avaria)
        session.commit()
        session.refresh(avaria)
        return avaria.id
    
    @classmethod
    def obter_avaria(cls, session, id):
         avaria = session.query(Avaria).filter(Avaria.id == id).first()
         return avaria
    
    @classmethod
    def listar_avarias(cls, session):
        avarias = session.query(Avaria).all()
        return avarias
    
    @classmethod
    def listar_ultima_avaria(cls, session):
        avarias = session.query(Avaria).order_by(Avaria.id.desc()).first()
        return avarias