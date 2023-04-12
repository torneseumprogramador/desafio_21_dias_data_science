import pyodbc
import models.pessoa as model

class PersistenciaSQLServer:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def conectar(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=' + self.host + ';'
                'DATABASE=' + self.database + ';'
                'UID=' + self.user + ';'
                'PWD=' + self.password + ';'
            )
        except pyodbc.Error as err:
            print("Erro ao conectar ao banco de dados:", err)

    def desconectar(self):
        if self.conn is not None:
            self.conn.close()

    def incluir_pessoa(self, pessoa):
        self.conectar()
        cursor = self.conn.cursor()
        query = "INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)"
        values = (pessoa.nome, pessoa.idade, pessoa.cidade)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def alterar_pessoa(self, pessoa):
        self.conectar()
        cursor = self.conn.cursor()
        query = "UPDATE pessoas SET nome = ?, idade = ?, cidade = ? WHERE id = ?"
        values = (pessoa.nome, pessoa.idade, pessoa.cidade, pessoa.id)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def excluir_pessoa(self, id):
        self.conectar()
        cursor = self.conn.cursor()
        query = "DELETE FROM pessoas WHERE id = ?"
        values = (id,)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def listar_pessoas(self):
        self.conectar()
        cursor = self.conn.cursor()
        query = "SELECT id, nome, idade, cidade FROM pessoas"
        cursor.execute(query)
        pessoas = []
        for id, nome, idade, cidade in cursor:
            pessoa = model.Pessoa(id, nome, idade, cidade)
            pessoas.append(pessoa)
        cursor.close()
        self.desconectar()
        return pessoas
