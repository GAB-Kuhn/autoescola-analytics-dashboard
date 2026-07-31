import pandas as pd
from sqlalchemy import create_engine

USUARIO_MYSQL = 'root'         
SENHA_MYSQL   = 'admin123'     
HOST_MYSQL    = 'localhost'     
PORTA_MYSQL   = '3306'          
BANCO_MYSQL   = 'autoescola_db' 

string_conexao = f"mysql+pymysql://{USUARIO_MYSQL}:{SENHA_MYSQL}@{HOST_MYSQL}:{PORTA_MYSQL}/{BANCO_MYSQL}"
engine = create_engine(string_conexao)

nome_arquivo = 'Dados Autoescola.xlsx'

excel_file = pd.ExcelFile(nome_arquivo)

for aba in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=aba)
    
    df.to_sql(name=aba, con=engine, if_exists='replace', index=False)
    print(f"Tabela '{aba}' importada com sucesso ({len(df)} registros).")

print("\nSem erros!")