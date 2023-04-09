import mysql.connector
from mysql.connector import errorcode
import models.pessoa as model

class PersistenciaMySQL:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def conectar(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro de acesso ao banco de dados. Verifique as credenciais de acesso.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
            else:
                print(err)

    def desconectar(self):
        if self.conn is not None and self.conn.is_connected():
            self.conn.close()

    def incluir_pessoa(self, pessoa):
        self.conectar()
        cursor = self.conn.cursor()
        query = "INSERT INTO pessoas (nome, idade, cidade) VALUES (%s, %s, %s)"
        values = (pessoa.nome, pessoa.idade, pessoa.cidade)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def alterar_pessoa(self, pessoa):
        self.conectar()
        cursor = self.conn.cursor()
        query = "UPDATE pessoas SET nome = %s, idade = %s, cidade = %s WHERE id = %s"
        values = (pessoa.nome, pessoa.idade, pessoa.cidade, pessoa.id)
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()
        self.desconectar()

    def excluir_pessoa(self, id):
        self.conectar()
        cursor = self.conn.cursor()
        query = "DELETE FROM pessoas WHERE id = %s"
        values = (id)
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
