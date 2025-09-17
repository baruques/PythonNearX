def main():
    listadetarefas = []

    while True:
        opcaoescolhida = menu()

        if opcaoescolhida == '1':
            vertarefas(listadetarefas)
        elif opcaoescolhida == '2':
            adicionartarefa(listadetarefas)
        elif opcaoescolhida == '3':
            removertarefa(listadetarefas)
        elif opcaoescolhida == '4':
            concluirtarefa(listadetarefas)
        elif opcaoescolhida == '5':
            sair()
            break       
        
def menu() -> str:

    opcoesdict = {
        "1" : "Ver tarefas",
        "2" : "Adicionar tarefa",
        "3" : "Remover tarefa",
        "4" : "Concluir tarefa",
        "5" : "Sair"    
    }

    imprimirmenu(opcoesdict)

    return selectoption(opcoesdict)

def selectoption(opcoesdict):
    while True:
        opcao = str(input("\nEscolha uma opção: "))
        if opcao not in opcoesdict.keys():
            print("\nOpção inválida. Tente novamente.\n")
        else:
            return opcao
    
def imprimirmenu(opcoesdict):
    print("\n--- App de Gerenciamento de Tarefas: ---")
    for index, op in opcoesdict.items():
        print(f"\nOpção {index}: {op}")

def vertarefas(listadetarefas):
    print("\n--- Lista de Tarefas ---")

    if not listadetarefas:
        print("\nNenhuma tarefa na lista.\n")
        return

    for i, tarefa in enumerate(listadetarefas):
        print(f"Tarefa {i+1}: {tarefa}")

def adicionartarefa(listadetarefas):
    tarefanova = str(input("\nQual é a tarefa a ser adicionada?"))
    listadetarefas.append(tarefanova)
    print("\nTarefa adicionada com sucesso!\n")
    input("Pressione Enter para continuar...")

def removertarefa(listadetarefas):
    vertarefas(listadetarefas)
    tarefaremovida = input("\nDigite o número da tarefa a ser removida: ")
    try:
        indice = int(tarefaremovida) - 1
        del listadetarefas[indice]
        print("\nTarefa removida com sucesso!\n")
        input("Pressione Enter para continuar...")
    except (ValueError, IndexError):
        print("\nFalha ao remover tarefa. O número digitado é inválido.\n")

def concluirtarefa(listadetarefas):
    vertarefas(listadetarefas)
    tarefaconcluida = input("\nDigite o número da tarefa a ser concluída: ")
    try:
        indice = int(tarefaconcluida) - 1
        del listadetarefas[indice]
        print("\nTarefa concluída e removida da lista.\n")
        input("Pressione Enter para continuar...")
    except (ValueError, IndexError):
        print("\nFalha ao concluir tarefa. O número digitado é inválido.\n")

def sair():
    print("\nSaindo do programa. Até mais!\n")
if __name__ == "__main__":
    main()