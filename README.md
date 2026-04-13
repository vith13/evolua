# 📚 Evolua – Seu Gestor de Estudos

> *Organize, acompanhe, evolua.*

O **Evolua** é uma aplicação web minimalista para gestão de estudos, desenvolvida como alternativa ao MyStudyLife com foco em acessibilidade para usuários lusófonos, estabilidade e simplicidade de uso.

---

## ✨ Funcionalidades

- ✅ Interface 100% em português
- 📋 Gerenciamento de tarefas (adicionar, concluir, excluir e filtrar)
- 📖 Cadastro de disciplinas (criar, editar e excluir)
- ⏱️ Registro de sessões de estudo por disciplina
- 🎯 Modo foco *(em desenvolvimento)*
- 📊 Relatório semanal *(em desenvolvimento)*
- ☁️ Backup manual dos dados *(em desenvolvimento)*

---

## 🛠️ Tecnologias utilizadas

- **Python** + **Flask** — backend e rotas
- **HTML** + **CSS** — interface
- **JavaScript** — interatividade do front-end
- **Jinja2** — templates HTML com herança (`base.html`)
- **Lucide Icons** — ícones
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
│   │   ├── tarefas.css
│   │   ├── disciplinas.css
│   │   ├── sessoes.css
│   │   └── login.css
│   └── img/
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── tarefas.html
│   ├── disciplinas.html
│   └── sessoes.html
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
| `/dashboard` | Painel principal |
| `/tarefas` | Gerenciamento de tarefas |
| `/disciplinas` | Cadastro de disciplinas |
| `/sessoes` | Registro de sessões de estudo |

---

## 👩‍💻 Autora

**Emilly Vitória Santana Alves**  
O projeto está sendo desenvolvido para a disciplina de Projeto de Software.
