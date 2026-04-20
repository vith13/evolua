from flask import Flask, render_template, request, jsonify, session, redirect
from services.sistema import SistemaEstudos
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "evolua_secret_key"

from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import os
from dotenv import load_dotenv
load_dotenv()

# CONFIGURAÇÃO DO EMAIL
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.secret_key)

sistema = SistemaEstudos()


# ============================================================
# PROTEÇÃO DE ROTAS
# ============================================================
def login_obrigatorio(f):
    @wraps(f)
    def verificar(*args, **kwargs):
        if "usuario" not in session:
            return redirect("/")
        return f(*args, **kwargs)
    return verificar


# ============================================================
# ROTAS DE TELAS
# ============================================================
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/esqueci-senha")
def esqueci_senha():
    return render_template("esqueci-senha.html")

@app.route("/dashboard")
@login_obrigatorio
def dashboard():
    nome = session.get("usuario", "Usuário")
    return render_template("dashboard.html", pagina_ativa="dashboard", nome=nome)

@app.route("/tarefas")
@login_obrigatorio
def tarefas():
    nome = session.get("usuario", "Usuário")
    return render_template("tarefas.html", pagina_ativa="tarefas", nome=nome)

@app.route("/disciplinas")
@login_obrigatorio
def disciplinas():
    nome = session.get("usuario", "Usuário")
    return render_template("disciplinas.html", pagina_ativa="disciplinas", nome=nome)

@app.route("/sessoes")
@login_obrigatorio
def sessoes():
    nome = session.get("usuario", "Usuário")
    return render_template("sessoes.html", pagina_ativa="sessoes", nome=nome)

@app.route("/foco")
@login_obrigatorio
def foco():
    nome = session.get("usuario", "Usuário")
    return render_template("foco.html", pagina_ativa="foco", nome=nome)

@app.route("/relatorio")
@login_obrigatorio
def relatorio():
    nome = session.get("usuario", "Usuário")
    return render_template("relatorio.html", pagina_ativa="relatorio", nome=nome)

@app.route("/calendario")
@login_obrigatorio
def calendario():
    nome = session.get("usuario", "Usuário")
    return render_template("calendario.html", pagina_ativa="calendario", nome=nome)

@app.route("/configuracoes")
@login_obrigatorio
def configuracoes():
    nome = session.get("usuario", "Usuário")
    email = session.get("email", "")
    return render_template("configuracoes.html", pagina_ativa="configuracoes", nome=nome, email=email)


# ============================================================
# API — AUTENTICAÇÃO
# ============================================================
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/api/cadastrar", methods=["POST"])
def api_cadastrar():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")

    for u in sistema.dados["usuarios"]:
        if u["email"] == email:
            return jsonify({"erro": "Email já cadastrado!"}), 400

    senha_hash = generate_password_hash(senha)
    sistema.dados["usuarios"].append({"nome": nome, "email": email, "senha": senha_hash})
    sistema._salvar()
    return jsonify({"sucesso": "Usuário cadastrado!"})

@app.route("/api/login", methods=["POST"])
def api_login():
    dados = request.get_json()
    email = dados.get("email")
    senha = dados.get("senha")

    for u in sistema.dados["usuarios"]:
        if u["email"] == email and check_password_hash(u["senha"], senha):
            session["usuario"] = u["nome"]
            session["email"] = u["email"]
            return jsonify({"sucesso": "Login realizado!", "nome": u["nome"]})

    return jsonify({"erro": "Email ou senha incorretos!"}), 401

@app.route("/api/logout")
def api_logout():
    session.clear()
    return redirect("/")


# ============================================================
# API — DISCIPLINAS
# ============================================================
@app.route("/api/disciplinas", methods=["GET"])
def api_listar_disciplinas():
    return jsonify(sistema.listar_disciplinas())

@app.route("/api/disciplinas", methods=["POST"])
def api_cadastrar_disciplina():
    dados = request.get_json()
    resultado = sistema.cadastrar_disciplina(dados["nome"], dados.get("cor", "#093952"))
    return jsonify(resultado)

@app.route("/api/disciplinas", methods=["PUT"])
def api_editar_disciplina():
    dados = request.get_json()
    resultado = sistema.editar_disciplina(dados["nome_atual"], dados["novo_nome"], dados["nova_cor"])
    return jsonify(resultado)

@app.route("/api/disciplinas/<nome>", methods=["DELETE"])
def api_remover_disciplina(nome):
    resultado = sistema.remover_disciplina(nome)
    return jsonify(resultado)


# ============================================================
# API — TAREFAS
# ============================================================
@app.route("/api/tarefas", methods=["GET"])
def api_listar_tarefas():
    return jsonify(sistema.listar_tarefas())

@app.route("/api/tarefas", methods=["POST"])
def api_adicionar_tarefa():
    dados = request.get_json()
    resultado = sistema.adicionar_tarefa(dados["nome"])
    return jsonify(resultado)

@app.route("/api/tarefas/<int:index>/concluir", methods=["PUT"])
def api_concluir_tarefa(index):
    resultado = sistema.concluir_tarefa(index)
    return jsonify(resultado)

@app.route("/api/tarefas/<int:index>", methods=["DELETE"])
def api_remover_tarefa(index):
    resultado = sistema.remover_tarefa(index)
    return jsonify(resultado)


# ============================================================
# API — SESSÕES
# ============================================================
@app.route("/api/sessoes", methods=["GET"])
def api_listar_sessoes():
    return jsonify(sistema.listar_sessoes())

@app.route("/api/sessoes", methods=["POST"])
def api_registrar_sessao():
    dados = request.get_json()
    resultado = sistema.registrar_sessao(
        dados["disciplina"],
        dados.get("horas", 0),
        dados.get("minutos", 0),
        dados.get("data"),
        dados.get("foco", False)
    )
    return jsonify(resultado)

@app.route("/api/sessoes/<int:index>", methods=["DELETE"])
def api_remover_sessao(index):
    resultado = sistema.remover_sessao(index)
    return jsonify(resultado)


# ============================================================
# API — EVENTOS
# ============================================================
@app.route("/api/eventos", methods=["GET"])
def api_listar_eventos():
    return jsonify(sistema.listar_eventos())

@app.route("/api/eventos", methods=["POST"])
def api_adicionar_evento():
    dados = request.get_json()
    resultado = sistema.adicionar_evento(
        dados["data"],
        dados["texto"],
        dados.get("disciplina", "")
    )
    return jsonify(resultado)

@app.route("/api/eventos/<data>/<int:index>", methods=["DELETE"])
def api_remover_evento(data, index):
    resultado = sistema.remover_evento(data, index)
    return jsonify(resultado)


# ============================================================
# API — RELATÓRIO
# ============================================================
@app.route("/api/relatorio", methods=["GET"])
def api_relatorio():
    periodo = request.args.get("periodo", "semana")
    disciplina = request.args.get("disciplina")
    resultado = sistema.gerar_relatorio(periodo, disciplina)
    return jsonify(resultado)


# ============================================================
# API — BACKUP
# ============================================================
@app.route("/api/backup", methods=["GET"])
def api_exportar_backup():
    return jsonify(sistema.exportar_backup())

@app.route("/api/backup", methods=["POST"])
def api_importar_backup():
    dados = request.get_json()
    resultado = sistema.importar_backup(dados)
    return jsonify(resultado)

#============================================
#REDEFINIÇAO DE SENHA
#============================================

@app.route("/api/esqueci-senha", methods=["POST"])
def api_esqueci_senha():
    dados = request.get_json()
    email = dados.get("email")

    usuario = next((u for u in sistema.dados["usuarios"] if u["email"] == email), None)
    if not usuario:
        # Por segurança, não revelamos se o email existe ou não
        return jsonify({"sucesso": "Se o email estiver cadastrado, você receberá as instruções."})

    token = serializer.dumps(email, salt="recuperar-senha")
    link = f"http://127.0.0.1:5000/redefinir-senha/{token}"

    msg = Message(
        subject="Evolua — Redefinição de senha", sender=os.getenv('MAIL_USERNAME'),
        recipients=[email],
        html=f"""
        <div style="font-family: 'League Spartan', sans-serif; max-width: 480px; margin: auto; padding: 32px; background: #f7f9fb; border-radius: 12px;">
            <h2 style="color: #093952;">Redefinir sua senha</h2>
            <p style="color: #555;">Recebemos uma solicitação para redefinir a senha da sua conta no <strong>Evolua</strong>.</p>
            <p style="color: #555;">Clique no botão abaixo para criar uma nova senha. O link expira em <strong>1 hora</strong>.</p>
            <a href="{link}" style="display:inline-block; margin: 20px 0; padding: 12px 24px; background: #093952; color: white; border-radius: 8px; text-decoration: none; font-weight: 700;">
                Redefinir senha
            </a>
            <p style="color: #aaa; font-size: 12px;">Se você não solicitou a redefinição, ignore este email.</p>
        </div>
        """
    )
    mail.send(msg)
    return jsonify({"sucesso": "Email enviado com sucesso!"})


@app.route("/redefinir-senha/<token>")
def redefinir_senha(token):
    try:
        email = serializer.loads(token, salt="recuperar-senha", max_age=3600)
    except:
        return render_template("login.html", erro="Link inválido ou expirado!")
    return render_template("redefinir-senha.html", token=token)


@app.route("/api/redefinir-senha", methods=["POST"])
def api_redefinir_senha():
    from werkzeug.security import generate_password_hash
    dados = request.get_json()
    token = dados.get("token")
    nova_senha = dados.get("senha")

    try:
        email = serializer.loads(token, salt="recuperar-senha", max_age=3600)
    except:
        return jsonify({"erro": "Link inválido ou expirado!"}), 400

    for u in sistema.dados["usuarios"]:
        if u["email"] == email:
            u["senha"] = generate_password_hash(nova_senha)
            sistema._salvar()
            return jsonify({"sucesso": "Senha redefinida com sucesso!"})

    return jsonify({"erro": "Usuário não encontrado!"}), 404


if __name__ == "__main__":
    app.run(debug=True)