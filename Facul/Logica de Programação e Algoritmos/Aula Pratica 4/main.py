import functions

file = "C:\Programacao\Portifolio\Facul\Logica de Programação e Algoritmos\Aula Pratica 4\colection.txt"
if functions.file_exists(file):
    print(f"Arquivo '{file}' encontrado. Carregando dados...")
else:
    print(f"Arquivo '{file}' não encontrado. Criando um novo arquivo...")
    functions.create_file(file)

opcao = functions.menu()

while True:
    opcao = functions.op_menu()
    if opcao == "1":
        functions.cadastrar_game()
    elif opcao == "2":
        functions.listar_games()
    elif opcao == "3":
        print("\nEncerrando o programa... Até mais!\n\n")
        break
    else:
        print("\nOpção inválida. Tente novamente.\n\n")
