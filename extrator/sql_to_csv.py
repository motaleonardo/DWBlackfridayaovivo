import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
import sys

load_dotenv(find_dotenv())

# Carregando variáveis de ambiente AWS
user = os.getenv("USER_AWS")
password = os.getenv("PASSWORD_AWS")
host = os.getenv("HOST_AWS")
port = os.getenv("PORT_AWS")
database = os.getenv("DATABASE_AWS")
nome_tabela = os.getenv("NOME_TABELA")

if not all([user, password, host, port, database, nome_tabela]):
    print("Erro: Variáveis de ambiente faltando.")
    sys.exit(1)

# database engine
url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(url)

# Query que busca os dados da tabela
query = f"SELECT * FROM {nome_tabela}"

try:
    # Lendo a tabela e salvando em um arquivo csv
    df = pd.read_sql(query, engine)
    
    # Criando diretório se não existir
    os.makedirs("./extracoes", exist_ok=True)
    
    # Salvando o arquivo csv
    df.to_csv(f"./extracoes/{nome_tabela}.csv", index=False)
    
    # Mensagem de sucesso
    print(f"Arquivo {nome_tabela}.csv criado com sucesso!")
except Exception as e:
    print(f"Erro ao executar a query ou salvar o arquivo CSV: {e}")
    sys.exit(1)