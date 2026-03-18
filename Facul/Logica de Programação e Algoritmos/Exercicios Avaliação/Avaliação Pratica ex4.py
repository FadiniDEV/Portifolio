#Variaveis globais definidas para funcionar a lista de contatos
lista_contatos = []
id_global = int(5479381)

#Função para cadastrar contatos que recebe o parametro do id_global para atribuir um id a cada contato
def cadastrar_contato(id):
    print("\n\n")
    print("-" * 41)
    print("-" * 10,"Cadastro de Contato", "-" * 10)
    id_contato = id
    nome = input("\nNome: ")
    atividade = input("Atividade: ")
    telefone = input("Telefone: ")

    contato = {"id": id_contato, "nome": nome, "atividade": atividade, "telefone": telefone}
    lista_contatos.append(contato.copy())
    
    print("\nContato cadastrado com sucesso!\n\n")

#Função de consultar contatos com varias opções de filtros para consulta
def consultar_contato():
    while True:
        print("\n\n")
        print("-" * 44)
        print("-" * 10,"Consulta de Contato(s)", "-" * 10)
        print("\n1 - Consultar Todos")
        print("2 - Consultar por ID")
        print("3 - Consultar por Atividade")
        print("4 - Voltar ao Menu Principal\n")

        try:
            op = int(input("Digite a opção desejada: "))

            #Consulta todos os contatos cadastrados
            if op == 1:
                if lista_contatos:
                    print("\nLista de Contatos:\n")
                    for contato in lista_contatos:
                        print("-" * 30)
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("-" * 30, "\n")
                else:
                    print("\nNenhum contato cadastrado.\n")

            #Consulta um contato específico pelo ID
            elif op == 2:
                id_consulta = int(input("\nDigite o ID do contato: "))
                encontrado = False
                for contato in lista_contatos:
                    if contato["id"] == id_consulta:
                        print("\nContato encontrado:\n")
                        print("-" * 30)
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("-" * 30, "\n")
                        encontrado = True
                        break
                if not encontrado:
                    print("\nContato não encontrado.\n")

            #Consulta contatos por atividade, lista todos os contatos com a mesma atividade
            elif op == 3:
                atividade_consulta = input("\nDigite a atividade do contato: ")
                encontrados = [contato for contato in lista_contatos if contato["atividade"].lower() == atividade_consulta.lower()]
                
                if encontrados:
                    print(f"\nContatos com atividade '{atividade_consulta}':\n")
                    for contato in encontrados:
                        print("-" * 30)
                        print(f"ID: {contato['id']}")
                        print(f"Nome: {contato['nome']}")
                        print(f"Atividade: {contato['atividade']}")
                        print(f"Telefone: {contato['telefone']}")
                        print("-" * 30, "\n")
                else:
                    print(f"\nNenhum contato encontrado com a atividade '{atividade_consulta}'.\n")

            #Opção para voltar ao menu
            elif op == 4:
                print("Voltando ao Menu Principal...\n\n")
                return

        #2 tipos de validações no programa para evitar crashes
            else:
                print("Opção inválida. Por favor, digite uma das opções acima.\n\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número correspondente às opções.\n\n")


#Função que verifica o id que o usuario digitou e se ele existir na lista de contatos, ele é removido
def remover_contato():
    print("\n\n")
    print("-" * 37)
    print("-" * 10,"Remover Contato", "-" * 10)
    id_remover = int(input("\nDigite o ID do contato a ser removido: "))
    
    for contato in lista_contatos:
        if contato["id"] == id_remover:
            lista_contatos.remove(contato)
            print("\nContato removido com sucesso!\n\n")
            return
    
    print("\nContato não encontrado. Nenhum contato foi removido.\n\n")

#Programa Principal
print("\n\nBem vindo a lista de contatos do Lucas Fadini Apolinário")


while True:

    #Print do menu principal
    print("-" * 36)
    print("-" * 10, "Menu Principal", "-" * 10)
    print("\n1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair\n")
    
    #Validação para evitar crashes caso o usuário digite algo diferente de um número inteiro
    try:
        op = int(input("Digite a opção desejada: "))

        if op == 1:
            cadastrar_contato(id_global)
            id_global += 1 #Incrementa o id_global para garantir que cada contato tenha um ID único
            
        elif op == 2:
            consultar_contato()

        elif op == 3:
                remover_contato()

        elif op == 4:
            print("Obrigado por usar a lista de contatos!\n\n")
            break
        else:
            print("Opção inválida. Por favor, digite uma das opções acima.\n\n")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número correspondente às opções.\n\n")