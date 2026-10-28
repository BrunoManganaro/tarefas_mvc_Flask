from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def test():
    return "Servidor online!"

@app.route('/')
def home():
    return render_template("base.html", titulo="Minha Lista de Tarefas")

if __name__ == "__main__":
    app.run()