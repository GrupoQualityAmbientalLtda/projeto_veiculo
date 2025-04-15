from src.dao.dao_usuario import DaoUsuario
from src.models.usuario import Usuario
from src.database.db import create_session
import pandas as pd

class ControllerUsuario:
    @classmethod
    def validar_campos_usuario (cls, nome, login, senha, permissao, status):
        if not nome:
            return "Nome não pode estar vazio!"
        if not login:
            return "Login não pode estar vazio!"
        if not senha:
            return "Senha não pode estar vazia!"
        if not permissao:
            return "Senha não pode estar vazia!"
        if not status:
            return "Senha não pode estar vazia!"
        return True
    
    @classmethod
    def cadastrar_usuario (cls, nome, login, senha, permissao, status):
        # Validação dos campos
        campos_validados = cls.validar_campos_usuario(nome, login, senha, permissao, status)
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
            return True
        
        except Exception as e:
            session.rollback()
            print(f"Erro gerado {e}")
            return False
        finally:
            session.close()
    
    @classmethod
    def obter_usuarios(cls):
        with create_session() as session:
            try:
                usuarios = DaoUsuario.listar_todos(session)
                return usuarios
            except Exception as e:
                return []
    @classmethod
    def listar_usuarios(cls):
        with create_session() as session:
            usuarios = cls.obter_usuarios()
            lista_usuarios = []
            for usuario in usuarios:
                lista_usuarios.append((usuario.id, 
                                       usuario.nome, 
                                       usuario.login, 
                                       usuario.permissao.value if hasattr(usuario.permissao, "value") else str(usuario.permissao),
                                       usuario.status.value if hasattr(usuario.status, "value") else str(usuario.status)))
            return lista_usuarios
    @classmethod
    def atualizar_usuario_pelo_id(cls, id, novo_nome, novo_login, nova_senha,nova_permissao, novo_status):
        with create_session() as session:
            try:
                DaoUsuario.atualizar_usuario_pelo_id(session, id, novo_nome, novo_login, nova_senha, nova_permissao, novo_status)
                session.commit()
                return True
            except Exception as e:
                print(f'Erro gerado {e}')
                session.rollback()
                return None

    @classmethod
    def carregar_dataframe_usuarios(cls):
        with create_session() as session:
            usuarios = DaoUsuario.listar_todos(session)

            dataframe_usuario = pd.DataFrame([
                {
                    "ID": usuario.id,
                    "Login": usuario.login,
                    "Nome": usuario.nome,
                    "Senha": usuario.senha,
                    "Permissao": usuario.permissao,
                    "Status": usuario.status.value if usuario.status else None
                }
                for usuario in usuarios
            ])
            dataframe_usuario['Seleção'] = False
            dataframe_usuario = dataframe_usuario.reindex(columns=['Seleção', 'ID', 'Login', 'Nome', 'Senha', 'Permissao', 'Status'])
            return dataframe_usuario
