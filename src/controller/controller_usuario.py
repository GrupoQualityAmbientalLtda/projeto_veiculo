from src.dao.dao_usuario import DaoUsuario
from src.models.usuario import Usuario
from src.database.db import create_session

class ControllerUsuario:
    @classmethod
    def validar_campos_usuario (cls, nome, login, senha, permissao, status):
        if not nome:
            return "Nome não pode estar vazio!"
        if not login:
            return "Login não pode estar vazio!"
        if not senha:
            return "Senha não pode estar vazia!"
        return True
    
    @classmethod
    def cadastrar_usuario (cls, nome, login, senha, permissao, status):
        # Validação dos campos
        campos_validados = cls.validar_campos_usuario(nome, login, senha)
        if campos_validados != True:
            return campos_validados
        
        # Criando a sessão, caso os campos sejam validados

        session = create_session()

        try:
            DaoUsuario.criar_usuario(session = session, 
                                     nome = nome,
                                     login = login,
                                     senha = senha,
                                     permissao = permissao,
                                     status = status)
            session.commit()
            return True # Por que os return Trues?
        
        except Exception as e:
            session.rollback()
            print(f"Erro gerado {e}")
            return False
        finally:
            session.close()        