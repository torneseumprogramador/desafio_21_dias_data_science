with open('vitimas_de_covid_brasil_2020.csv', mode='r') as file:
    # Lê as linhas do arquivo
    lines = file.readlines()

    # Remove a primeira linha, que contém os nomes das colunas
    lines.pop(0)

    # Percorre as linhas e exibe na tela
    for line in lines:
        # Remove o caractere de quebra de linha do final da linha
        line = line.strip()

        # Divide a linha pelos separadores vírgula
        fields = line.split(',')

        # Exibe os campos
        print(f'ID: {fields[0]}, Cidade: {fields[1]}, Estado: {fields[2]}, Número de vítimas: {fields[3]}')
