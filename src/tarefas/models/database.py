import mysql.connector as mc
from mysql.connector import Error


class Database:
    def __init__(self):
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'admin'
        self.database = 'app_viagens'
        self.connection = None
        self.cursos = None

    def conectar(self):
        try:
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )

            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None

    def desconectar(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print('Conexão encerrada com sucesso!')

# Área 13
db = Database()
db.conectar()
db.desconectar()