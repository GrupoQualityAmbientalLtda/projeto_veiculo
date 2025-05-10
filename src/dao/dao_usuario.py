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
    
    @classmethod
    def listar_todos(cls, session):
        usuario = session.query(Usuario).order_by(Usuario.id).all()
        return usuario
    
    @classmethod
    def atualizar_usuario_pelo_id(cls, session, id, novo_nome, novo_login, nova_senha, nova_permissao, novo_status):
        usuario = session.query(Usuario).filter(Usuario.id == id).first()
        usuario.nome = novo_nome
        usuario.login = novo_login
        usuario.senha = nova_senha
        usuario.permissao = nova_permissao
        usuario.status = novo_status
        session.add(usuario)
        return usuario