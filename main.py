import os 

def exibir_tarefas(tarefas): 
    print("\n--- Lista de Tarefas ---")
    for i, tarefas in enumerate(tarefas, 1): 
        print(f"{i}. {tarefas}")
    print("------------------------")

def adicionar_tarefas(tarefas, nova_tarefa):
    tarefas.append(nova_tarefa)
    print(f'Tarefa "{nova_tarefa}" adicionada com sucesso!')

def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice - 1)
        print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
    else:
        print("Índice inválido. Tarefa não removida.")

def main(): 
    tarefas = []

    while True: 
        print("\nEscolha uma opção:")
        print("1. Exibir Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Remover Tarefa")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            exibir_tarefas(tarefas)
        elif opcao == "2":
            nova_tarefa = input("Digite a nova tarefa: ")
            adicionar_tarefas(tarefas, nova_tarefa)
        elif opcao == "3": 
            indice = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif opcao == "4": 
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()