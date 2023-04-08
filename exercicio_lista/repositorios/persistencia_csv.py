import csv
import os

import models.pessoa as model


class PersistenciaCsv:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_arquivo)
        self.pessoas = []
        
    def incluir_pessoa(self, pessoa):
        with open(self.arquivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([pessoa.nome, pessoa.idade, pessoa.cidade])
        
    def alterar_pessoa(self, pessoa):
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for p in self.pessoas:
                if p[0] == pessoa.nome:
                    writer.writerow([pessoa.nome, pessoa.idade, pessoa.cidade])
                else:
                    writer.writerow(p)
        
    def excluir_pessoa(self, nome):
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for p in self.pessoas:
                if p[0] != nome:
                    writer.writerow(p)
        
    def listar_pessoas(self):
        self.carregar_dados()
        lista_instancia_pessoas = []
        for p in self.pessoas:
            pessoa = model.Pessoa(nome=p[0], idade=p[1], cidade=p[2])
            lista_instancia_pessoas.append(pessoa)
        return lista_instancia_pessoas
        
    def carregar_dados(self):
        self.pessoas = []
        try:
            with open(self.arquivo, mode='r') as file:
                reader = csv.reader(file)
                next(reader) # ignora a primeira linha (header)
                for row in reader:
                    self.pessoas.append(row)
        except FileNotFoundError:
            self.pessoas = []
        