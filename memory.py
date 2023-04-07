# Criando um objeto do tipo bytes
b = bytes([0, 1, 2, 3, 4])

# Criando um objeto memoryview a partir do objeto bytes
mv = memoryview(b)

# Modificando o segundo byte do objeto bytes por meio do objeto memoryview
# mv[1] = 9

# Imprimindo o objeto bytes modificado
print(b)  # Saída: b'\x00\t\x02\x03\x04'
print(mv[1])
