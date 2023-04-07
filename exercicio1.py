while True:
    opcao1 = int(input("Digite a primeira opção: "))
    opcao2 = int(input("Digite a segunda opção: "))
    opcao3 = int(input("Digite a terceira opção: "))
    opcao4 = int(input("Digite a quarta opção: "))
    opcao5 = int(input("Digite a quinta opção: "))

    if opcao1 == 5 or opcao1 == 33 or opcao1 == 90 or opcao1 == 10:
        print("Parabéns, você acertou um dos números premiados!")
    elif opcao2 == 5 or opcao2 == 33 or opcao2 == 90 or opcao2 == 10:
        print("Parabéns, você acertou um dos números premiados!")
    elif opcao3 == 5 or opcao3 == 33 or opcao3 == 90 or opcao3 == 10:
        print("Parabéns, você acertou um dos números premiados!")
    elif opcao4 == 5 or opcao4 == 33 or opcao4 == 90 or opcao4 == 10:
        print("Parabéns, você acertou um dos números premiados!")
    elif opcao5 == 5 or opcao5 == 33 or opcao5 == 90 or opcao5 == 10:
        print("Parabéns, você acertou um dos números premiados!")
    else:
        print("Você não acertou nenhum dos números premiados.")

    sair = input("Digite 0 para sair: \n")
    if sair == "0":
        break
