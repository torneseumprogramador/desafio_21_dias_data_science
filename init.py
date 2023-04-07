import locale

# Definindo a localização do sistema como "pt_BR.UTF-8"
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("Olá João, vamos armazenar os seus produtos?")
nome = input("Digite o nome do produto:\n")
valor_str = input("Digite o valor do produto:\n")
valor_str = valor_str.replace(".", "").replace(",", ".").replace("R$", "")
valor = float(valor_str)

valor_formatado = locale.currency(valor, grouping=True, symbol=None)
print(f"Seu produto, {nome}, no valor de R$ {valor_formatado} foi armazenado com sucesso!")
# print(f"Seu produto, {nome}, no valor de R$ {valor:.2f} foi armazenado com sucesso!")
# print("Seu produto, " + nome + ", no valor de R$ " + str(valor) + " foi armazenado com sucesso!")
# print("Seu produto, {}, no valor de R$ {} foi armazenado com sucesso!".format(nome, valor))



# x = 42
# y = '10'

# print("O tipo de x:")
# print(type(x))

# print("O tipo de y:")
# print(type(y))

# print("A soma de x + y:")
# print(x + int(y))
