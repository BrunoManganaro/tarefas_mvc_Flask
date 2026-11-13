from flask import Flask, redirect, render_template, request, url_for

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return "Servidor online!"

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # Casa com o nome do input no form
        data_conclusao_form = request.form['dataConclusao'] # Casa com o nome do input no form

        data_corrigida = data_conclusao_form or None
        # 'or' nesse caso é um operador de coalescência -> retorna o 
        # primeiro valor válido

        # Instanciamos uma nova tarefa com os dados recebidos do form
        tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa no banco
        tarefa.salvarTarefa()

        return redirect(url_for('home'))

    tarefas = Tarefa.listarTarefas()

    return render_template(
        "base.html",
        titulo_da_pagina="Minha Lista de Tarefas",
        tarefas_da_pagina=tarefas,
        botao_submit="Adicionar",
        botao_voltar="display: none",
        h1_pagina="Digite a tarefa e a data de conclusão:"
    )

@app.route('/delete/<int:id>')
def apagar_id_especificado(id = None):
    url = request.path
    Tarefa.apagarTarefas(url)
    return(redirect(url_for('home')))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar_id_especificado(id = None):
    url = request.path
    
    if request.method == 'POST':
        titulo_form = request.form['tituloTarefa'] # Casa com o nome do input no form
        data_conclusao_form = request.form['dataConclusao'] # Casa com o nome do input no form

        data_corrigida = data_conclusao_form or None
        # 'or' nesse caso é um operador de coalescência -> retorna o 
        # primeiro valor válido

        # Instanciamos uma nova tarefa com os dados recebidos do form
        #tarefa = Tarefa(titulo=titulo_form, data_conclusao=data_corrigida)

        # Salvamos a tarefa no banco
        Tarefa.editarTarefas(url, titulo_form, data_corrigida)

        return redirect(url_for('home'))

    return render_template(
        "base.html",
        titulo_da_pagina="Minha Lista de Tarefas",
        tarefas_da_pagina={"titulo_tarefa":None, "data_conclusao":None},
        botao_submit="Atualizar",
        h1_pagina="Edite sua tarefa:",
        lista="display: none"
    )

if __name__ == "__main__":
    app.run()