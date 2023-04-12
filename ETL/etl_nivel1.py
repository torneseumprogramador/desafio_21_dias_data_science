import csv

# passo a passo de um processo ETL

# ===== inicio "Extract" =======
lista_vitimas_covid = []
with open('vitimas_de_covid_brasil_2020.csv', mode='r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)  # pula a primeira linha (cabeçalho)
    for row in csv_reader:
        lista_vitimas_covid.append({
            "id": row[0],
            "cidade": row[1],
            "estado": row[2],
            "vitimas": row[3],
        })
# ===== fim "Extract" =======

# print(type(lista_vitimas_covid))
# print(type(lista_vitimas_covid[0]))

# mostre na tela todas as vitimas do estado SP

# ===== inicio "Transform" =======
lista_vitimas_sp = {}
for vitima in lista_vitimas_covid:
    if vitima["estado"] == "SP":
        vitimas_somadas = int(lista_vitimas_sp["SP"]["vitimas"]) if "SP" in lista_vitimas_sp and lista_vitimas_sp["SP"] is not None else 0

        lista_vitimas_sp["SP"] = {
            "cidade": vitima["cidade"],
            "estado": vitima["estado"],
            "vitimas": int(vitima["vitimas"]) + vitimas_somadas
        }

# ===== fim "Transform" =======

print(lista_vitimas_sp)