import csv
import os
import uuid

import models.pessoa as model


class PersistenciaCsv:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_arquivo)
        self.pessoas = []
        
    def incluir_pessoa(self, pessoa):
        with open(self.arquivo, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([uuid.uuid4(), pessoa.nome, pessoa.idade, pessoa.cidade])
        
    def alterar_pessoa(self, pessoa):
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for p in self.pessoas:
                if p[0] == pessoa.id:
                    writer.writerow([pessoa.id, pessoa.nome, pessoa.idade, pessoa.cidade])
                else:
                    writer.writerow(p)
        
    def excluir_pessoa(self, id):
        with open(self.arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for p in self.pessoas:
                if p[0] != id:
                    writer.writerow(p)
        
    def listar_pessoas(self):
        self.carregar_dados()
        lista_instancia_pessoas = []
        for p in self.pessoas:
            pessoa = model.Pessoa(id=p[0], nome=p[1], idade=p[2], cidade=p[3])
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
        