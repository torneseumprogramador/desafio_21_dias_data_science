import pandas as pd

df = pd.read_csv('vitimas_de_covid_brasil_2020.csv', sep=',')
print(df) # print de um dataframe pandas, dataframe = tabela de dados em memória

# for index, row in df.iterrows():
#     print(f'ID: {row["id"]}, Cidade: {row["cidade"]}, Estado: {row["estado"]}, Número de vítimas: {row["numero_de_vitimas"]}')
