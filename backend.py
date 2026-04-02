import json
from datetime import datetime

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

    def cadastrar_disciplina(self, nome):
        for d in self.dados["disciplinas"]:
            if d["nome"]== nome:
                return "Disciplina já existe!"
        self.dados["disciplinas"].append({
            "nome": nome
       })
        self.salvar_dados()
        return "Disciplina cadastrada com sucesso!"
    
    def registrar_sessao(self, disciplina, duracao_minutos):
     sessao = {
        "disciplina": disciplina,
        "duracao": duracao_minutos,
        "data": datetime.now().strftime("%Y-%m-%d")
     }

     self.dados["sessoes"].append(sessao)
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
    
    def adicionar_tarefa(self, tarefa):
     self.dados["tarefas"].append({
        "tarefa": tarefa
    })
     self.salvar_dados()
     return "Tarefa adicionada!"
    
    def backup_manual(self):
     with open("backup.json", "w") as f:
        json.dump(self.dados, f, indent=4)

     return "Backup criado com sucesso!"
    
    def relatorio_semanal(self):
     total = sum(s["duracao"] for s in self.dados["sessoes"])
     return f"Total estudado na semana: {total} minutos"
    
    def filtrar_por_periodo(self, periodo):
     return f"Filtro aplicado: {periodo}"



pass
    
    
if __name__ == "__main__":
    sistema = SistemaEstudos()

    while True:
        print("\n=== SISTEMA DE ESTUDOS ===")
        print("1. Cadastrar disciplina")
        print("2. Registrar sessão de estudo")
        print("3. Ver horas por disciplina")
        print("4. Disciplina mais estudada")
        print("5. Relatório semanal")
        print("6. Filtro por período")
        print("7. Lista de tarefas")
        print("8. Backup manual")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da disciplina: ")
            print(sistema.cadastrar_disciplina(nome))

        elif opcao == "2":
            disciplina = input("Disciplina: ")
            duracao = int(input("Duração (minutos): "))
            print(sistema.registrar_sessao(disciplina, duracao))

        elif opcao == "3":
            disciplina = input("Disciplina: ")
            total = sistema.calcular_horas_por_disciplina(disciplina)
            print(f"Total: {total} minutos")

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
            print(sistema.backup_manual())

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")