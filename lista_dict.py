
pessoas = [] 
while True:
    print("-"* 20)
    print("O que você deseja fazer ?")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input()
    if opcao == "1":
        pessoa = {}
        pessoa["nome"] = input("Digite o nome:\n")
        pessoa["idade"] = input("Digite a idade:\n")
        pessoa["cidade"] = input("Digite a cidade:\n")

        pessoas.append(pessoa) # usando lista de dict
    elif opcao == "2":
        for pessoa in pessoas:
            print("-"* 20)
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Cidade: {pessoa['cidade']}")
    elif opcao == "3":
        break