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


if __name__ == "__main__":
    app.run(debug=True)

