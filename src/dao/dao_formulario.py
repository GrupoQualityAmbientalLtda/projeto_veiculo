from src.models.formulario import Formulario

class DaoFormulario:
    @classmethod
    def criar_formulario(cls, session, id_usuario, id_veiculo, id_tipo, id_status, data):
        formulario = Formulario(
            id_usuario=id_usuario,
            id_veiculo=id_veiculo,
            id_tipo=id_tipo,
            id_status=id_status,
            data=data
        )
        session.add(formulario)
        session.commit()
        return formulario
    @classmethod
    def obter_formulario_por_id(cls, session, id):
        """
        Obtém um formulário pelo ID.
        """
        formulario = session.query(Formulario).filter(Formulario.id == id).first()
        return formulario

    @classmethod
    def listar_formularios_por_veiculo(cls, session, id_veiculo):
        """
        Lista todos os formulários associados a um veículo.
        """
        formularios = session.query(Formulario).filter(Formulario.id_veiculo == id_veiculo).all()
        return formularios
