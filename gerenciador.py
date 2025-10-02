def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")


def ver_tarefas(tarefas):
    print("\nLista de Tarefas: ")
    if not tarefas:  # verifica se a lista está vazia
        print("Nenhuma tarefa cadastrada.")
    else:
        for indice, tarefa in enumerate(tarefas):
            status = "Completada" if tarefa["completada"] else "Pendente"
            print(f"{indice + 1}. {tarefa['tarefa']} - {status}")


def atualizar_tarefa(tarefas, indice, novo_nome):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["tarefa"] = novo_nome
        print(f"Tarefa {indice + 1} atualizada para '{novo_nome}'")
    else:
        print("Índice inválido.")


def completar_tarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["completada"] = True
        print(f"Tarefa {indice + 1} marcada como completada.")
    else:
        print("Índice inválido.")


def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    print("Tarefas completadas deletadas.")


# Função auxiliar para validar número
def obter_indice(mensagem, tarefas):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            indice = int(entrada) - 1
            if 0 <= indice < len(tarefas):
                return indice
            else:
                print("Número fora do intervalo. Tente novamente.")
        else:
            print("Digite apenas números.")


# Programa principal
tarefas = []
while True:
    print("\nMenu do Gerenciador de Tarefas: ")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == '1':
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == '2':
        ver_tarefas(tarefas)

    elif escolha == '3':
        ver_tarefas(tarefas)
        if tarefas:
            indice = obter_indice("Digite o número da tarefa que deseja atualizar: ", tarefas)
            novo_nome = input("Digite o novo nome da tarefa: ")
            atualizar_tarefa(tarefas, indice, novo_nome)

    elif escolha == '4':
        ver_tarefas(tarefas)
        if tarefas:
            indice = obter_indice("Digite o número da tarefa que deseja completar: ", tarefas)
            completar_tarefa(tarefas, indice)

    elif escolha == '5':
        deletar_tarefas_completadas(tarefas)

    elif escolha == '6':
        print("\nPrograma encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
