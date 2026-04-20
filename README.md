# 📚 Evolua – Seu Gestor de Estudos

> *Organize, acompanhe, evolua.*

O **Evolua** é uma aplicação web minimalista para gestão de estudos, desenvolvida como alternativa ao MyStudyLife com foco em acessibilidade para usuários lusófonos, estabilidade e simplicidade de uso.

---

## ✨ Funcionalidades

- ✅ Interface 100% em português
- 🏠 Dashboard com visão geral, gráfico de disciplinas, tarefas, modo foco e calendário
- 📋 Gerenciamento de tarefas (adicionar, concluir, excluir e filtrar)
- 📖 Cadastro de disciplinas com cores personalizadas (criar, editar e excluir)
- ⏱️ Registro de sessões de estudo por disciplina
- 🎯 Modo foco com timer, Pomodoro e salvamento automático de sessão
- 📊 Relatório de horas estudadas com gráfico e filtros por dia, semana e mês
- 📅 Calendário com compromissos e sessões de estudo por disciplina
- 🔍 Barra de pesquisa global (tarefas, disciplinas, sessões e compromissos)
- ☁️ Backup manual — exportar e importar dados em JSON
- ⚙️ Configurações de perfil, dados e conta
- 🔐 Autenticação com cadastro, login e recuperação de senha por email
- 🛡️ Proteção de rotas — acesso restrito a usuários autenticados
- 🔒 Senhas criptografadas com hash seguro

---

## 🛠️ Tecnologias utilizadas

- **Python** + **Flask** — backend e rotas
- **HTML** + **CSS** — interface
- **JavaScript** — interatividade do front-end
- **Jinja2** — templates HTML com herança (`base.html`)
- **Lucide Icons** — ícones
- **Chart.js** — gráficos de relatório e dashboard
- **Flask-Mail** — envio de emails para recuperação de senha
- **Werkzeug** — criptografia de senhas
- **itsdangerous** — geração de tokens seguros para redefinição de senha
- **python-dotenv** — gerenciamento seguro de variáveis de ambiente
- **JSON** — persistência de dados no servidor

---

## 🧠 Conceitos de POO aplicados

| Conceito | Onde foi aplicado |
|---|---|
| **Classe** | `Entidade`, `Disciplina`, `Tarefa`, `Sessao`, `Usuario`, `Relatorio` |
| **Herança** | `Disciplina`, `Tarefa`, `Sessao`, `SessaoFoco`, `Evento` herdam de `ItemEstudo` |
| **Abstrato** | `ItemEstudo` é abstrata com métodos `to_dict()` e `resumo()` obrigatórios |
| **Polimorfismo** | `resumo()` se comporta diferente em `Sessao`, `SessaoFoco`, `Tarefa` e `Evento` |
| **Overloading** | `Relatorio.gerar()` aceita parâmetros opcionais `periodo` e `disciplina` |

---

## 📁 Estrutura do projeto

```
projeto_software/
│
├── data/
│   └── dados.json
│
├── models/
│   └── models.py
│
├── services/
│   └── sistema.py
│
├── static/
│   ├── css/
│   │   ├── dashboard.css
│   │   ├── dashboard_page.css
│   │   ├── tarefas.css
│   │   ├── disciplinas.css
│   │   ├── sessoes.css
│   │   ├── foco.css
│   │   ├── relatorio.css
│   │   ├── calendario.css
│   │   ├── configuracoes.css
│   │   └── login.css
│   └── img/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── cadastro.html
│   ├── esqueci-senha.html
│   ├── redefinir-senha.html
│   ├── dashboard.html
│   ├── tarefas.html
│   ├── disciplinas.html
│   ├── sessoes.html
│   ├── foco.html
│   ├── relatorio.html
│   ├── calendario.html
│   └── configuracoes.html
│
├── app.py
├── backend.py
├── .env              
├── .gitignore
└── README.md
```

---

## ▶️ Como executar o projeto

### Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- pip (gerenciador de pacotes do Python, já vem com o Python)
- Uma conta Gmail com senha de app configurada (para recuperação de senha)

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/vith13/evolua.git
cd evolua
```

**2. Crie e ative um ambiente virtual** *(recomendado)*
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install flask flask-mail werkzeug itsdangerous python-dotenv
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```
MAIL_USERNAME=seuemail@gmail.com
MAIL_PASSWORD=suasenhadapp
```

**5. Execute a aplicação**
```bash
python app.py
```

**6. Acesse no navegador**
```
http://127.0.0.1:5000
```

---

## 🗺️ Rotas disponíveis

| Rota | Descrição |
|---|---|
| `/` | Tela de login |
| `/cadastro` | Cadastro de novo usuário |
| `/esqueci-senha` | Solicitação de redefinição de senha |
| `/redefinir-senha/<token>` | Redefinição de senha via token |
| `/dashboard` | Painel principal |
| `/tarefas` | Gerenciamento de tarefas |
| `/disciplinas` | Cadastro de disciplinas |
| `/sessoes` | Registro de sessões de estudo |
| `/foco` | Modo foco com timer |
| `/relatorio` | Relatório de horas estudadas |
| `/calendario` | Calendário com compromissos |
| `/configuracoes` | Configurações da conta |

---

## 🔌 API disponível

| Método | Rota | Descrição |
|---|---|---|
| POST | `/api/cadastrar` | Cadastrar usuário |
| POST | `/api/login` | Fazer login |
| GET | `/api/logout` | Encerrar sessão |
| GET/POST | `/api/disciplinas` | Listar ou criar disciplina |
| PUT | `/api/disciplinas` | Editar disciplina |
| DELETE | `/api/disciplinas/<nome>` | Remover disciplina |
| GET/POST | `/api/tarefas` | Listar ou criar tarefa |
| PUT | `/api/tarefas/<index>/concluir` | Concluir tarefa |
| DELETE | `/api/tarefas/<index>` | Remover tarefa |
| GET/POST | `/api/sessoes` | Listar ou registrar sessão |
| DELETE | `/api/sessoes/<index>` | Remover sessão |
| GET/POST | `/api/eventos` | Listar ou adicionar evento |
| DELETE | `/api/eventos/<data>/<index>` | Remover evento |
| GET | `/api/relatorio` | Gerar relatório |
| GET/POST | `/api/backup` | Exportar ou importar backup |

---

## 🔮 Melhorias futuras

- 🌙 Tema escuro
- 📱 Versão responsiva para celular
- 🔔 Notificações de lembrete de estudo
- 📅 Integração com Google Calendar
- 🌐 Lançamento como SaaS com planos e autenticação real
- 🗄️ Migração para banco de dados relacional (PostgreSQL)

---

## 👩‍💻 Autora

**Emilly Vitória Santana Alves**  
Projeto desenvolvido para a disciplina de Projeto de Software.
