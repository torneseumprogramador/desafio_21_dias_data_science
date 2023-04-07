import os
import time


def cadastra_pessoa(pessoas):
    os.system('clear')
    print("CADASTRO DE USUÁRIO\n")
    pessoa = {}
    pessoa["nome"] = input("Digite o nome: ")
    pessoa["idade"] = input("Digite a idade: ")
    pessoa["cidade"] = input("Digite a cidade: ")
    pessoas.append(pessoa) # usando lista de dict
    print("\nUsuário cadastrado com sucesso!")
    time.sleep(2) # espera 2 segundos antes de voltar para o menu
    return pessoas

def mostra_pessoas(pessoas):
    os.system('clear')
    print("LISTA DE USUÁRIOS\n")
    if len(pessoas) == 0:
        print("Não há usuários cadastrados.")
    else:
        for pessoa in pessoas:
            print("-" * 20)
            retorno = pessoa_formatada(pessoa)
            print(retorno)
    input("\nPressione Enter para voltar ao menu...")

def pessoa_formatada(pessoa):
    # return f"Nome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nCidade: {pessoa['cidade']}"
    return f"""
Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
Cidade: {pessoa['cidade']}
    """
