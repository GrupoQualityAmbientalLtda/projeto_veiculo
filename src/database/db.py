from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# dados do banco de dados
engine = create_engine('sqlite:///data/banco_de_dados.db', echo=True)

Base = declarative_base()

# cria a sessão para interação com o banco de dados
def create_session():
  Session = sessionmaker(bind=engine)
  session = Session()
  return session

# cria as tabelas do banco de dados
def create_tables():
  Base.metadata.create_all(engine) 
