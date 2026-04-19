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

---

## 🛠️ Tecnologias utilizadas

- **Python** + **Flask** — backend e rotas
- **HTML** + **CSS** — interface
- **JavaScript** — interatividade do front-end
- **Jinja2** — templates HTML com herança (`base.html`)
- **Lucide Icons** — ícones
- **Chart.js** — gráficos de relatório e dashboard
- **LocalStorage** — persistência temporária dos dados (front-end)

---

## 📁 Estrutura do projeto

```
projeto_software/
│
├── data/
│   └── dados.json
│
├── models/
├── services/
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
└── README.md
```

---

## ▶️ Como executar o projeto

### Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado
- pip (gerenciador de pacotes do Python, já vem com o Python)

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/evolua.git
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
pip install flask
```

**4. Execute a aplicação**
```bash
python app.py
```

**5. Acesse no navegador**
```
http://127.0.0.1:5000
```

---

## 🗺️ Rotas disponíveis

| Rota | Descrição |
|---|---|
| `/` | Tela de login |
| `/cadastro` | Cadastro de novo usuário |
| `/esqueci-senha` | Redefinição de senha |
| `/dashboard` | Painel principal |
| `/tarefas` | Gerenciamento de tarefas |
| `/disciplinas` | Cadastro de disciplinas |
| `/sessoes` | Registro de sessões de estudo |
| `/foco` | Modo foco com timer |
| `/relatorio` | Relatório de horas estudadas |
| `/calendario` | Calendário com compromissos |
| `/configuracoes` | Configurações da conta |

---

## 🔮 Melhorias futuras

- 🌙 Tema escuro
- 📱 Versão responsiva para celular
- 🔔 Notificações de lembrete de estudo
- 📅 Integração com Google Calendar
- 🌐 Lançamento como SaaS com planos e autenticação real

---

## 👩‍💻 Autora

**Emilly Vitória Santana Alves**  
Projeto desenvolvido para a disciplina de Projeto de Software.
