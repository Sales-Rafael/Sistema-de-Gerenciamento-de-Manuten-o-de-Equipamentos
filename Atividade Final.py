import random
lista_de_manutenção = []

def exibir_menu():
    while True:
        print("\nSistema de Gerenciamento de Manutenção de Equipamentos\n")
        print("1 - Adicionar manutenção realizada ao histórico")
        print("2 - Remover manutenção do histórico")
        print("3 - Listar histórico de manutenções realizadas")
        print("4 - Alterar manutenção realizada no histórico")
        print("0 - Sair")
        opcao = int(input("\nSelecione uma opção: "))
        if opcao == 1:
            adicionar_manutenção()
        elif opcao == 2:
            remover_manutenção()
        elif opcao == 3:
            consultando_lista_de_manutenções()
        elif opcao == 4:
            alterar_manutenção()
        elif opcao == 0:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, selecione uma opção válida.")

def dados():
    id= random.randint(10000,99999)
    nome_do_mecanico = input('\nDigite o nome do responsavel pela manutenção: ')
    while True:
        data = input("\nDigite a data da manutenção do equipamento (dd/mm/aaaa): ")
        if len(data) == 10 and data[2] == '/' and data[5] == '/':
            dia, mes, ano = data.split('/')
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 2100:
                    break
                else:
                    print("Data inválida: dia, mês ou ano fora do intervalo.")
            else:
                print("Data inválida: use apenas números.")
        else:
            print("Data inválida: siga o formato dd/mm/aaaa.")
    nome_do_maquinario = input('\nDigite o nome do maquinário: ')
    manutenção = {
        'ID': id,
        "Mecânico" : nome_do_mecanico,
        "Data": data,
        "Maquinário": nome_do_maquinario
    }
    return manutenção

def adicionar_manutenção():
    print('\nAdicionando nova manutenção. Siga as instruções...\n')
    manutenção =dados()
    lista_de_manutenção.append(manutenção)
    print('\nManutenção adicionada com sucesso\n')
    
def consultando_lista_de_manutenções():
    print('\n Lista de Manutenções Registradas \n')
    if not lista_de_manutenção:
        print("Nenhuma manutenção registrada no sistema.")
        return
    for item in lista_de_manutenção:
        print("---------------------------------------------")
        print(f"ID: {item['ID']}")
        print(f"Mecânico responsável: {item['Mecânico']}")
        print(f"Data: {item['Data']}")
        print(f"Maquinário: {item['Maquinário']}\n")

def remover_manutenção():
    if not lista_de_manutenção:
        print("\nNenhuma manutenção registrada para remover.")
        return
    id_remover = int(input("Digite o ID da manutenção que deseja remover: "))
    for i, manut in enumerate(lista_de_manutenção):
        if manut['ID'] == id_remover:
            confirm = input(f"Tem certeza que deseja remover a manutenção ID {id_remover}? (s/n): ").lower()
            if confirm == 's':
                lista_de_manutenção.pop(i)
                print(f"Manutenção ID {id_remover} removida com sucesso!")
            else:
                print("Remoção cancelada.")
            return
    print(f"Nenhuma manutenção encontrada com o ID {id_remover}.")
    
def alterar_manutenção():
    if not lista_de_manutenção:
        print("\nNenhuma manutenção registrada para alterar.")
        return
    id_alterar = int(input("Digite o ID da manutenção que deseja alterar: "))
    for i, manut in enumerate(lista_de_manutenção):
        if manut['ID'] == id_alterar:
            print("\nDigite os novos dados da manutenção (os campos anteriores serão substituídos):")
            nova_manutencao = dados()
            nova_manutencao['ID'] = id_alterar
            lista_de_manutenção[i] = nova_manutencao
            print("Manutenção alterada com sucesso!")
            return
    print(f"Nenhuma manutenção encontrada com o ID {id_alterar}.")

exibir_menu()
