import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine

load_dotenv(find_dotenv())
# Carregando variáveis de ambiente Render
database_url = os.getenv("DATABASE_URL")
nome_tabela = os.getenv("NOME_TABELA")

# Carregando variáveis de ambiente AWS
user = os.getenv("USER_AWS")
password = os.getenv("PASSWORD_AWS")
host = os.getenv("HOST_AWS")
port = os.getenv("PORT_AWS")
database = os.getenv("DATABASE_AWS")

# database engine
url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(database_url)

query = f"SELECT * FROM {nome_tabela}"

df = pd.read_sql(query, engine)

df.to_sql(nome_tabela, url, if_exists='replace', index=False)

print(f"Arquivo {nome_tabela} criado na AWS com sucesso!")