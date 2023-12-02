from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.prod")  # Carrega as variáveis de ambiente do arquivo .env

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Configurando a conexão com o banco de dados

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"    

# Criando a engine de conexão

engine = create_engine(DATABASE_URL)

# Criando a sessão

Session = sessionmaker(bind=engine)

Base = declarative_base()


# Definindo o modelo de dados
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)


# Criando a tabela
Base.metadata.create_all(bind=engine)