import os
import time

import models.pessoa as models

import repositorios.persistencia_mysql as repo

# import repositorios.persistencia_csv as repo
# import repositorios.persistencia_json as repo

repoInstancia = repo.PersistenciaMySQL("localhost", "desafio_data_science", "root", "root")
# repoInstancia = repo.PersistenciaCsv("pessoas.csv")
# repoInstancia = repo.PersistenciaJson("pessoas.json")

def cadastra_pessoa():
    os.system('clear')
    print("CADASTRO DE USUÁRIO\n")
    pessoa = models.Pessoa()
    pessoa.nome = input("Digite o nome: ")
    pessoa.idade = input("Digite a idade: ")
    pessoa.cidade = input("Digite a cidade: ")
    
    repoInstancia.incluir_pessoa(pessoa)

    print("\nUsuário cadastrado com sucesso!")
    time.sleep(2) # espera 2 segundos antes de voltar para o menu

def mostra_pessoas():
    pessoas = repoInstancia.listar_pessoas()
    
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
    # return f"Id: {pessoa.id}\nNome: {pessoa.nome}\nIdade: {pessoa.idade}\nCidade: {pessoa.cidade}"
    return f"""
Id: {pessoa.id}
Nome: {pessoa.nome}
Idade: {pessoa.idade}
Cidade: {pessoa.cidade}
    """
