from src.models.formulario import Formulario

class DaoFormulario:
    @classmethod
    #ADICIONAR DESTINOS e OBS e IMAGENS
    def criar_formulario(cls, session, id_usuario, id_veiculo, tipo, data, id_revisao):
        formulario = Formulario(
            id_usuario=id_usuario,
            id_veiculo=id_veiculo,
            tipo=tipo,
            data=data,
            id_revisao=id_revisao
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
