import random

estados = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'CE', 'PE', 'AM']

with open('vitimas_de_covid_brasil_2020_exemplo2.csv', mode='w') as file:
    file.write('id,cidade,estado,numero_de_vitimas\n')
    for i in range(1, 101):
        cidade = f"Cidade {i}"
        estado = random.choice(estados)
        numero_de_vitimas = random.randint(1, 100)
        file.write(f"{i},{cidade},{estado},{numero_de_vitimas}\n")
print('Arquivo gerado com sucesso!')
