# Criando um objeto do tipo range com início 0, fim 10 (exclusivo) e passo 2
r = range(0, 10, 2)

# Iterando sobre o objeto range e imprimindo seus valores
for i in r:
    print(i)

# Saída: 0 2 4 6 8

# Verificando se um valor está contido no objeto range
tem_4 = 4 in r
tem_5 = 5 in r

print(tem_4)  # Saída: True
print(tem_5)  # Saída: False
