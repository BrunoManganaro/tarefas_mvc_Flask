from datetime import datetime

from tarefas.models.database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperar e processar os dados das
    tarefas criadas a partir do formulário principal.
    """

    def __init__(self, titulo, id = None, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""

        sql = "INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s);"
        params = (self.titulo, self.data_conclusao) # protegem contra SQL Injection

        # Gerenciador de contexto (with)
        # Acessa os métodos __enter__ e __exit__ da classe
        with Database() as db:
            db.executar(sql, params)


# Área 13 (testes)
tarefa = Tarefa("Minha nova tarefa")
tarefa.salvarTarefa()