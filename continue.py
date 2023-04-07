i = 1

while True:
    if i % 2 == 1: # comparação para impar
    # if i % 2 == 0: # comparação para par
        i += 1
        continue

    print(i)

    if i >= 1000:
        break

    i += 1