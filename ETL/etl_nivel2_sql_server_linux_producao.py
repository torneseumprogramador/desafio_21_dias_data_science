# importar dados para o SQL Server

# caso o pandas não esteja instalado, rodar os comandos abaixo no servidor linux
# sudo apt install python3-pip
# sudo apt install unixodbc-dev 
# https://learn.microsoft.com/pt-br/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline
# pip install pyodbc

import os

import pandas as pd
import pyodbc

###### ETL ######

#### Extract #####
# Lendo o arquivo CSV usando o método read_csv
df = pd.read_csv("vitimas_de_covid_brasil_2020.csv")
#### Extract #####


#### Transform #####
grouped = df.groupby(['cidade', 'estado']).agg({'numero_de_vitimas':'sum'})
#### Transform #####


#### Load #####
# Lê as variáveis de ambiente
server = os.environ['HOST']
database = os.environ['DATABASE']
username = os.environ['USER']
password = os.environ['PASS']

# Conecta com o banco de dados usando as variáveis de ambiente
conn = pyodbc.connect(f"Driver={{ODBC Driver 18 for SQL Server}};"
                      f"Server=tcp:{server},1433;"
                      f"Database={database};"
                      f"Uid={username};"
                      f"Pwd={password};"
                      f"Encrypt=yes;"
                      f"TrustServerCertificate=no;"
                      f"Connection Timeout=30;")

# Loop através de cada linha no DataFrame
for row in grouped.iterrows():
    cidade = row[0][0]
    estado = row[0][1]
    vitimas = row[1][0]
    
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
    print(f"Vitimas: {vitimas}")
    
    # sql = f"INSERT INTO vitimas_covid (cidade,estado,vitimas) VALUES ('{cidade}', '{estado}', {vitimas})"
    # print(sql)
    # conn.execute(sql)
    
    print("-" * 60)
    # Inserindo uma linha na tabela
    conn.execute("INSERT INTO vitimas_covid (cidade,estado,vitimas) VALUES (?, ?, ?)", cidade, estado, int(vitimas))

# Salvando as mudanças
conn.commit()

# Fechando a conexão
conn.close()
#### Load #####