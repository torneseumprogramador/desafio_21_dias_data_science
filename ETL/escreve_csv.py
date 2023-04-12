import csv
import random

estados = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'CE', 'PE', 'AM']

with open('vitimas_de_covid_brasil_2020.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['id', 'cidade', 'estado', 'numero_de_vitimas'])
    for i in range(1, 101):
        cidade = f"Cidade {i}"
        estado = random.choice(estados)
        numero_de_vitimas = random.randint(1, 100)
        writer.writerow([i, cidade, estado, numero_de_vitimas])
print('Arquivo gerado com sucesso!')
