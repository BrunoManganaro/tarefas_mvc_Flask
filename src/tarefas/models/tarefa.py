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
        params = (self.titulo, self.data_conclusao) # protege contra SQL Injection

        # Gerenciador de contexto (with)
        # Acessa os métodos __enter__ e __exit__ da classe
        with Database() as db:
            db.executar(sql, params)

    @staticmethod
    def listarTarefas() -> list:
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao FROM tarefa 
        LIMIT 100;'''
        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def apagarTarefas(id):
        novo_id = id[8:]
        sql = f'DELETE FROM tarefa WHERE id_tarefa = {int(novo_id)};'
        with Database() as db:
            db.executar(sql)

    @staticmethod
    def editarTarefas(id, titulo, data):
        novo_id = id[6:]
        sql = 'UPDATE tarefa SET titulo_tarefa = %s, data_conclusao = %s WHERE id_tarefa = %s;'
        params = (titulo, data, novo_id)
        with Database() as db:
            return(db.executar(sql, params))


# Área 13 (testes)
# tarefa = Tarefa("Minha nova tarefa")
# arefa.salvarTarefa()