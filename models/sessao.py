class SessaoEstudo:
    def __init__(self, id, disciplina_id, data, duracao):
        self.id = id
        self.disciplina_id = disciplina_id
        self.data = data
        self.duracao = duracao

    def __str__(self):
        return f"{self.data} | Disciplina {self.disciplina_id} | {self.duracao}h"