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

Todos os conceitos estão implementados em `models/models.py` e utilizados em `services/sistema.py`.

---

### 🔷 Classe Abstrata

A classe `ItemEstudo` é a base abstrata do sistema. Por ser abstrata (usando `ABC` do Python), ela **não pode ser instanciada diretamente** — serve apenas como modelo para as subclasses.

Ela define dois métodos abstratos obrigatórios que toda subclasse deve implementar:

```python
class ItemEstudo(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @abstractmethod
    def resumo(self) -> str:
        pass
```

---

### 🔷 Herança

As classes `Disciplina`, `Tarefa`, `Sessao`, `SessaoFoco` e `Evento` herdam de `ItemEstudo`, reaproveitando seus atributos (`nome`, `criado_em`) e sendo obrigadas a implementar `to_dict()` e `resumo()`.

`SessaoFoco` vai além e herda de `Sessao`, que já herda de `ItemEstudo` — demonstrando herança em dois níveis:

```python
class Sessao(ItemEstudo):       # herda de ItemEstudo
    ...

class SessaoFoco(Sessao):       # herda de Sessao → herança em cadeia
    ...
```

---

### 🔷 Polimorfismo

O método `resumo()` é implementado de forma diferente em cada subclasse. O mesmo método, chamado em objetos de tipos diferentes, produz respostas distintas.

Isso é invocado em `services/sistema.py` na função `registrar_sessao()`:

```python
def registrar_sessao(self, disciplina, horas, minutos, data=None, foco=False):
    if foco:
        sessao = SessaoFoco("Sessão Foco", disciplina, horas, minutos, data)
    else:
        sessao = Sessao("Sessão", disciplina, horas, minutos, data)

    # POLIMORFISMO — mesmo método, comportamento diferente por tipo de objeto
    print(f"[POLIMORFISMO] {sessao.resumo()}")
```

Saída ao registrar uma **sessão normal**:
```
[POLIMORFISMO] Sessão: Matemática | 1h 30min | 2026-04-23
```

Saída ao registrar uma **sessão de foco (Pomodoro)**:
```
[POLIMORFISMO] Sessão Foco: Matemática | 0h 25min | 2026-04-23 🎯
```

Outros exemplos de `resumo()` polimórfico:

```python
Tarefa("Estudar Flask").resumo()
# → "Tarefa: Estudar Flask [❌ Pendente]"

Disciplina("Matemática", "#093952").resumo()
# → "Disciplina: Matemática (cor: #093952)"

Evento("Prova Final", "2026-04-30", "Cálculo").resumo()
# → "Compromisso: Prova Final (Cálculo) | 2026-04-30"
```

---

### 🔷 Overloading

Em Python, o overloading é feito com parâmetros opcionais. O método `gerar()` da classe `Relatorio` funciona de formas diferentes dependendo dos argumentos passados:

```python
class Relatorio:
    def gerar(self, periodo: str = "semana", disciplina: str = None) -> dict:
        ...
```

Pode ser chamado de três formas:

```python
relatorio.gerar()                          # relatório semanal, todas as disciplinas
relatorio.gerar("mes")                     # relatório mensal, todas as disciplinas
relatorio.gerar("dia", "Matemática")       # relatório diário, só Matemática
```

---

### Resumo visual

| Conceito | Arquivo | Onde |
|---|---|---|
| **Classe abstrata** | `models/models.py` | Classe `ItemEstudo` com `@abstractmethod` |
| **Herança simples** | `models/models.py` | `Disciplina`, `Tarefa`, `Sessao`, `Evento` → `ItemEstudo` |
| **Herança em cadeia** | `models/models.py` | `SessaoFoco` → `Sessao` → `ItemEstudo` |
| **Polimorfismo** | `models/models.py` + `services/sistema.py` | Método `resumo()` com comportamentos distintos, invocado em `registrar_sessao()` |
| **Overloading** | `models/models.py` | `Relatorio.gerar()` com parâmetros opcionais |

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
├── .env              ← NÃO suba para o GitHub
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
