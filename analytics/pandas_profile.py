import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from ydata_profiling import ProfileReport

# Load environment variables
load_dotenv(find_dotenv())

# Save profile report
try:

    # Generate profile report
    profile = ProfileReport(df, title="Google Analytics Data", title="Google Analytics Data")
    
    # Load data
    df = pd.read_csv("extracoes/google_analytics_data.csv")
    
    # Criando diretório se não existir
    os.makedirs("extracoes", exist_ok=True)
    
    # Salvando o arquivo csv
    profile.to_file("extracoes/google_analytics_data_profile.html")
    
    # Mensagem de sucesso
    print(f"Arquivo {nome_tabela}.csv criado com sucesso!")
except Exception as e:
    print(f"Erro ao executar a query ou salvar o arquivo CSV: {e}")
    sys.exit(1)
profile.to_file("extracoes/google_analytics_data_profile.html")