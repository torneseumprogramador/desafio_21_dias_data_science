import csv
import random

estados = {'AC': ['Rio Branco'], 
           'AL': ['Maceió'], 
           'AP': ['Macapá'], 
           'AM': ['Manaus'], 
           'BA': ['Salvador'], 
           'CE': ['Fortaleza'], 
           'ES': ['Vitória'], 
           'GO': ['Goiânia'], 
           'MA': ['São Luís'], 
           'MT': ['Cuiabá'], 
           'MS': ['Campo Grande'], 
           'MG': ['Belo Horizonte'], 
           'PA': ['Belém'], 
           'PB': ['João Pessoa'], 
           'PR': ['Curitiba'], 
           'PE': ['Recife'], 
           'PI': ['Teresina'], 
           'RJ': ['Rio de Janeiro'], 
           'RN': ['Natal'], 
           'RS': ['Porto Alegre'], 
           'RO': ['Porto Velho'], 
           'RR': ['Boa Vista'], 
           'SC': ['Florianópolis'], 
           'SP': ['São Paulo'], 
           'SE': ['Aracaju'], 
           'TO': ['Palmas']}

with open('vitimas_de_covid_brasil_2020.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['id', 'cidade', 'estado', 'numero_de_vitimas'])
    for i in range(1, 901):
        estado = random.choice(list(estados.keys()))
        cidade = random.choice(estados[estado])
        numero_de_vitimas = random.randint(1, 100)
        writer.writerow([i, cidade, estado, numero_de_vitimas])
print('Arquivo gerado com sucesso!')
