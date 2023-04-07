
pessoas = [] 
while True:
    print("-"* 20)
    print("O que você deseja fazer ?")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input()
    if opcao == "1":
        nome = input("Digite o nome:\n")
        idade = input("Digite a idade:\n")
        cidade = input("Digite a cidade:\n")

        pessoas.append([nome, idade, cidade]) # usando matriz
    elif opcao == "2":
        for pessoa in pessoas:
            print("-"* 20)
            print(f"Nome: {pessoa[0]}")
            print(f"Idade: {pessoa[1]}")
            print(f"Cidade: {pessoa[2]}")
    elif opcao == "3":
        break