import csv

with open('vitimas_de_covid_brasil_2020.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # pula a primeira linha (cabeçalho)
    for row in csv_reader:
        print(f'ID: {row[0]}, Cidade: {row[1]}, Estado: {row[2]}, Número de vítimas: {row[3]}')
