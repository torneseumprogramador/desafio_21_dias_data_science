import pessoas.funcoes as fnp
import telas.funcoes as fnt

pessoas = []

while True:
    fnt.menu()
    opcao = input()

    if opcao == "1":
        pessoas = fnp.cadastra_pessoa(pessoas)
    elif opcao == "2":
        fnp.mostra_pessoas(pessoas)
    elif opcao == "3":
        fnt.mensagem_com_pausa("Encerrando o programa...")
        break
    else:
        fnt.mensagem_com_pausa("Opção inválida. Tente novamente.")


