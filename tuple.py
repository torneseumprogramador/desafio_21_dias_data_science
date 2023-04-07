# Criando uma lista de frutas
frutas_lista = ['maçã', 'banana', 'laranja']

# Criando uma tupla de frutas
frutas_tupla = ('maçã', 'banana', 'laranja')

# Imprimindo a lista e a tupla
print('Lista de frutas:', frutas_lista)
print('Tupla de frutas:', frutas_tupla)

# Adicionando uma fruta à lista (válido)
frutas_lista.append('abacaxi')
print('Lista de frutas atualizada:', frutas_lista)

# Adicionando uma fruta à tupla (inválido)
# Isso vai gerar um TypeError: 'tuple' object has no attribute 'append'
# frutas_tupla.append('abacaxi')

# Tentando modificar uma fruta na tupla (inválido)
# Isso vai gerar um TypeError: 'tuple' object does not support item assignment
# frutas_tupla[0] = 'morango'
