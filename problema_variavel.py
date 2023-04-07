# Solicita ao usuário que insira 5 números inteiros
num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = int(input("Insira o terceiro número inteiro: "))
num4 = int(input("Insira o quarto número inteiro: "))
num5 = int(input("Insira o quinto número inteiro: "))

# Solicita ao usuário que insira 4 números decimais (floats)
num6 = float(input("Insira o primeiro número decimal: "))
num7 = float(input("Insira o segundo número decimal: "))
num8 = float(input("Insira o terceiro número decimal: "))
num9 = float(input("Insira o quarto número decimal: "))

# Soma todos os números
total = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9

# Exibe o resultado formatado na tela
print("A soma de todos os números é: {:.2f}".format(total))
