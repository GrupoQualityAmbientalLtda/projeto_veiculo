from src.models.formulario import Formulario

class DaoFormulario:
    @classmethod
    def criar_formulario(cls, session, id_usuario, id_veiculo, tipo, id_revisao, data, observacao):
        formulario = Formulario(
            id_usuario=id_usuario,
            id_veiculo=id_veiculo,
            tipo=tipo,
            id_revisao = id_revisao,
            data=data,
            observacao=observacao
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
    def listar_formularios_por_usuario(cls, session, id_usuario):
        """
        Lista todos os formulários associados a um usuário.
        """
        formularios = session.query(Formulario).filter(Formulario.id_usuario == id_usuario).all()
        return formularios
