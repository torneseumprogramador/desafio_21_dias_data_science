import os
import time


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
