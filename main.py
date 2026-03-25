from services.sistema import SistemaEstudos

sistema = SistemaEstudos()

def menu():
    print("\n--- EVOLUA ---")
    print("1 - Adicionar disciplina")
    print("2 - Listar disciplinas")
    print("3 - Registrar sessão")
    print("4 - Listar sessões")
    print("5 - Adicionar tarefa")
    print("6 - Listar tarefas")
    print("7 - Concluir tarefa")
    print("8 - Iniciar modo foco")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome da disciplina: ")
        sistema.adicionar_disciplina(nome)

    elif opcao == "2":
        sistema.listar_disciplinas()

    elif opcao == "3":
        disciplina_id = int(input("ID da disciplina: "))
        data = input("Data (YYYY-MM-DD): ")
        duracao = float(input("Horas: "))
        sistema.adicionar_sessao(disciplina_id, data, duracao)

    elif opcao == "4":
        sistema.listar_sessoes()

    elif opcao == "5":
        desc = input("Descrição da tarefa: ")
        sistema.adicionar_tarefa(desc)

    elif opcao == "6":
        sistema.listar_tarefas()

    elif opcao == "7":
        id_tarefa = int(input("ID da tarefa: "))
        sistema.concluir_tarefa(id_tarefa)

    elif opcao == "8":
        sistema.iniciar_modo_foco()

    elif opcao == "0":
        break