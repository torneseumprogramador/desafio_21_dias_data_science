import json
import os
import uuid

import models.pessoa as model


class PersistenciaJson:
    def __init__(self, nome_arquivo):
        caminho_projeto = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        self.arquivo = os.path.join(caminho_projeto, "db", nome_arquivo)
        self.pessoas = []
        
    def incluir_pessoa(self, pessoa):
        pessoa.id = uuid.uuid4()
        self.carregar_dados()
        self.pessoas.append(pessoa.__dict__)
        self.salvar_dados()
        
    def alterar_pessoa(self, pessoa):
        self.carregar_dados()
        for i, p in enumerate(self.pessoas):
            if p["id"] == pessoa.id:
                self.pessoas[i] = pessoa.__dict__
                self.salvar_dados()
                break
        
    def excluir_pessoa(self, id):
        self.carregar_dados()
        self.pessoas = [p for p in self.pessoas if p["id"] != id]
        self.salvar_dados()
        
    def listar_pessoas(self):
        self.carregar_dados()
        lista_instancia_pessoas = []
        for p in self.pessoas:
            pessoa = model.Pessoa(**p)
            lista_instancia_pessoas.append(pessoa)
        return lista_instancia_pessoas
        
    def carregar_dados(self):
        try:
            with open(self.arquivo, "r") as f:
                self.pessoas = json.load(f)
        except FileNotFoundError:
            self.pessoas = []
        
    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.pessoas, f)
