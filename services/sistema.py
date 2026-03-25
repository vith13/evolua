from models.disciplina import Disciplina
from models.sessao import SessaoEstudo
from models.tarefa import Tarefa
import time

class SistemaEstudos:
    def __init__(self):
        self.disciplinas = []
        self.sessoes = []
        self.tarefas = []

    def iniciar_modo_foco(self):
      if not self.disciplinas:
        print("Nenhuma disciplina cadastrada!")
        return

      print("\nDisciplinas:")
      for d in self.disciplinas:
        print(d)

      disciplina_id = int(input("Escolha o ID da disciplina: "))
      minutos = int(input("Duração do foco (minutos): "))

      print("\nModo foco iniciado...")

      for i in range(minutos, 0, -1):
        print(f"Tempo restante: {i} min")
        time.sleep(1)

      print("\nSessão de foco concluída! 🎯")

      from datetime import date
      hoje = str(date.today())
      horas = minutos / 60

      self.adicionar_sessao(disciplina_id, hoje, horas)

    # DISCIPLINAS
    def adicionar_disciplina(self, nome):
        novo_id = len(self.disciplinas) + 1
        disciplina = Disciplina(novo_id, nome)
        self.disciplinas.append(disciplina)
        print("Disciplina adicionada!")

    def listar_disciplinas(self):
        for d in self.disciplinas:
            print(d)

    # SESSÕES
    def adicionar_sessao(self, disciplina_id, data, duracao):
        novo_id = len(self.sessoes) + 1
        sessao = SessaoEstudo(novo_id, disciplina_id, data, duracao)
        self.sessoes.append(sessao)
        print("Sessão registrada!")

    def listar_sessoes(self):
        for s in self.sessoes:
            print(s)

    # TAREFAS
    def adicionar_tarefa(self, descricao):
        novo_id = len(self.tarefas) + 1
        tarefa = Tarefa(novo_id, descricao)
        self.tarefas.append(tarefa)
        print("Tarefa adicionada!")

    def listar_tarefas(self):
        for t in self.tarefas:
            print(t)

    def concluir_tarefa(self, id_tarefa):
        for t in self.tarefas:
            if t.id == id_tarefa:
                t.concluida = True
                print("Tarefa concluída!")


                
