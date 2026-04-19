from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", pagina_ativa="dashboard")

@app.route("/tarefas")
def tarefas():
    return render_template("tarefas.html", pagina_ativa="tarefas")

@app.route("/disciplinas")
def disciplinas():
    return render_template("disciplinas.html", pagina_ativa="disciplinas")

@app.route("/sessoes")
def sessoes():
    return render_template("sessoes.html", pagina_ativa="sessoes")

@app.route("/foco")
def foco():
    return render_template("foco.html", pagina_ativa="foco")

@app.route("/relatorio")
def relatorio():
    return render_template("relatorio.html", pagina_ativa="relatorio")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html", pagina_ativa="calendario")

@app.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes.html", pagina_ativa="configuracoes")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/esqueci-senha")
def esqueci_senha():
    return render_template("esqueci-senha.html")


if __name__ == "__main__":
    app.run(debug=True)

