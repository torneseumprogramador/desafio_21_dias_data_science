import os
import time


def cadastra_pessoa():
    os.system('clear')
    print("CADASTRO DE USUÁRIO\n")
    pessoa = {}
    pessoa["nome"] = input("Digite o nome: ")
    pessoa["idade"] = input("Digite a idade: ")
    pessoa["cidade"] = input("Digite a cidade: ")
    pessoas.append(pessoa) # usando lista de dict
    print("\nUsuário cadastrado com sucesso!")
    time.sleep(2) # espera 2 segundos antes de voltar para o menu

def mostra_pessoas():
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

def menu():
    os.system('clear') # limpa o console
    print("-" * 20)
    print("O que você deseja fazer?")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

def mensagem_com_pausa(msg):
    os.system('clear')
    print(msg)
    time.sleep(2) # espera 2 segundos antes de sair do programa

def pessoa_formatada(pessoa):
    # return f"Nome: {pessoa['nome']}\nIdade: {pessoa['idade']}\nCidade: {pessoa['cidade']}"
    return f"""
Nome: {pessoa['nome']}
Idade: {pessoa['idade']}
Cidade: {pessoa['cidade']}
    """

pessoas = []

while True:
    menu()
    opcao = input()

    if opcao == "1":
        cadastra_pessoa()
    elif opcao == "2":
        mostra_pessoas()
    elif opcao == "3":
        mensagem_com_pausa("Encerrando o programa...")
        break
    else:
        mensagem_com_pausa("Opção inválida. Tente novamente.")


