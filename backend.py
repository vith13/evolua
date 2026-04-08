import json
from datetime import datetime, timedelta
import time

#classe base
class Entidade:
    def __init__(self, nome):
        self.nome = nome


#classes filhas
class Disciplina(Entidade):
    def to_dict(self):
        return {"nome": self.nome}


class Tarefa(Entidade):
    def __init__(self, nome, concluida=False):
        super().__init__(nome)
        self.concluida = concluida

    def to_dict(self):
        return {
            "tarefa": self.nome,
            "concluida": self.concluida
        }


class Sessao:
    def __init__(self, disciplina, duracao, data=None):
        self.disciplina = disciplina
        self.duracao = duracao
        self.data = data or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "disciplina": self.disciplina,
            "duracao": self.duracao,
            "data": self.data
        }


#sistma
class SistemaEstudos:

    def __init__(self):
        self.arquivo = "data/dados.json"
        self.dados = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo, "r") as f:
                return json.load(f)
        except:
            return {
                "disciplinas": [],
                "sessoes": [],
                "tarefas": []
            }

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.dados, f, indent=4)

    #disciplinas
    def cadastrar_disciplina(self, nome):
        for d in self.dados["disciplinas"]:
            if d["nome"] == nome:
                return "Disciplina já existe!"

        disciplina = Disciplina(nome)
        self.dados["disciplinas"].append(disciplina.to_dict())
        self.salvar_dados()

        return "Disciplina cadastrada com sucesso!"

    def remover_disciplina(self, nome):
        self.dados["disciplinas"] = [
            d for d in self.dados["disciplinas"] if d["nome"] != nome
        ]
        self.salvar_dados()
        return "Disciplina removida!"

    #sessoes
    def registrar_sessao(self, disciplina, duracao_minutos, data=None):
        sessao = Sessao(disciplina, duracao_minutos, data)
        self.dados["sessoes"].append(sessao.to_dict())
        self.salvar_dados()

        return "Sessão registrada com sucesso!"

    def calcular_horas_por_disciplina(self, disciplina):
        total = 0
        for sessao in self.dados["sessoes"]:
            if sessao["disciplina"] == disciplina:
                total += sessao["duracao"]

        return f"{total} minutos"

    def disciplina_mais_estudada(self):
        contador = {}

        for sessao in self.dados["sessoes"]:
            d = sessao["disciplina"]
            contador[d] = contador.get(d, 0) + sessao["duracao"]

        if not contador:
            return "Nenhuma sessão registrada."

        mais = max(contador, key=contador.get)
        return f"Disciplina mais estudada: {mais}"

    # relatoriio
    def relatorio_semanal(self):
        hoje = datetime.now()
        limite = hoje - timedelta(days=7)

        total = sum(
            s["duracao"]
            for s in self.dados["sessoes"]
            if datetime.strptime(s["data"], "%Y-%m-%d") >= limite
        )

        return f"Total estudado na semana: {total} minutos"

    def filtrar_por_periodo(self, periodo):
        hoje = datetime.now()

        if periodo == "dia":
            limite = hoje - timedelta(days=1)
        elif periodo == "semana":
            limite = hoje - timedelta(days=7)
        elif periodo == "mes":
            limite = hoje - timedelta(days=30)
        else:
            return "Período inválido"

        filtradas = [
            s for s in self.dados["sessoes"]
            if datetime.strptime(s["data"], "%Y-%m-%d") >= limite
        ]

        if not filtradas:
            return "Nenhuma sessão encontrada."

        resultado = ""
        for s in filtradas:
            resultado += f"{s['disciplina']} - {s['duracao']} min - {s['data']}\n"

        return resultado

    #tarefas
    def adicionar_tarefa(self, tarefa):
        nova = Tarefa(tarefa)
        self.dados["tarefas"].append(nova.to_dict())
        self.salvar_dados()
        return "Tarefa adicionada!"

    def listar_tarefas(self):
        if not self.dados["tarefas"]:
            return "Nenhuma tarefa."

        resultado = ""
        for i, t in enumerate(self.dados["tarefas"]):
            status = "✔" if t["concluida"] else "❌"
            resultado += f"{i} - {t['tarefa']} [{status}]\n"

        return resultado

    def concluir_tarefa(self, index):
        try:
            self.dados["tarefas"][index]["concluida"] = True
            self.salvar_dados()
            return "Tarefa concluída!"
        except:
            return "Índice inválido."

    #backup e foco
    def backup_manual(self):
        with open("backup.json", "w") as f:
            json.dump(self.dados, f, indent=4)

        return "Backup criado com sucesso!"

    def modo_foco(self, disciplina, minutos):
        print(f"Foco iniciado em {disciplina} por {minutos} minutos...")
        time.sleep(minutos * 60)

        self.registrar_sessao(disciplina, minutos)
        return "Sessão de foco finalizada e registrada!"
    

    #menu
    
if __name__ == "__main__":
    sistema = SistemaEstudos()

    while True:
        print("\n=== SISTEMA DE ESTUDOS ===")
        print("1. Cadastrar disciplina")
        print("2. Registrar sessão")
        print("3. Ver horas por disciplina")
        print("4. Disciplina mais estudada")
        print("5. Relatório semanal")
        print("6. Filtro por período")
        print("7. Adicionar tarefa")
        print("8. Listar tarefas")
        print("9. Concluir tarefa")
        print("10. Modo foco")
        print("11. Remover disciplina")
        print("12. Backup")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome da disciplina: ")
            print(sistema.cadastrar_disciplina(nome))

        elif opcao == "2":
            disciplina = input("Disciplina: ")
            duracao = int(input("Duração (minutos): "))
            print(sistema.registrar_sessao(disciplina, duracao))

        elif opcao == "3":
            disciplina = input("Disciplina: ")
            print(sistema.calcular_horas_por_disciplina(disciplina))

        elif opcao == "4":
            print(sistema.disciplina_mais_estudada())

        elif opcao == "5":
            print(sistema.relatorio_semanal())

        elif opcao == "6":
            periodo = input("Digite (dia/semana/mes): ")
            print(sistema.filtrar_por_periodo(periodo))

        elif opcao == "7":
            tarefa = input("Digite a tarefa: ")
            print(sistema.adicionar_tarefa(tarefa))

        elif opcao == "8":
            print(sistema.listar_tarefas())

        elif opcao == "9":
            index = int(input("Índice da tarefa: "))
            print(sistema.concluir_tarefa(index))

        elif opcao == "10":
            disciplina = input("Disciplina: ")
            minutos = int(input("Minutos: "))
            print(sistema.modo_foco(disciplina, minutos))

        elif opcao == "11":
            nome = input("Nome da disciplina: ")
            print(sistema.remover_disciplina(nome))

        elif opcao == "12":
            print(sistema.backup_manual())

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")