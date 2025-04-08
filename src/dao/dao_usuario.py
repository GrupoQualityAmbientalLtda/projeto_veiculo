from src.models.usuario import Usuario

class DaoUsuario:
    @classmethod
    def criar_usuario(cls, session, login, senha, nome, permissao, status):
        usuario = Usuario(login = login, senha = senha, nome = nome, permissao = permissao, status = status)
        session.add(usuario)
        session.commit()
        return usuario
    
    @classmethod
    def obter_usuario(cls, session, id):
        usuario = session.query(Usuario).filter(Usuario.id == id).first()
        return usuario

    