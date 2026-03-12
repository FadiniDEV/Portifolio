def file_exists(filename):
    try:
        a = open (filename, "rt")
        a.close()
        return True
    except FileNotFoundError:
        return False
    

def create_file(filename):
    try:
        a = open (filename, "wt+")
        a.close()
    except Exception as e:
        print(f"Erro ao criar arquivo: {e}")
    else:
        print(f"Arquivo '{filename}' criado com sucesso!")


def menu():
    print("\n   Bem vindo meu grande colecionador!!\n\n\
    Menu:\n\
    1 - Cadastrar Games\n\
    2 - Listar Games\n\
    3 - Sair\n")


def op_menu():
    return input("Digite a opção desejada: ")


def cadastrar_game():
    print("\n\nCadastro de Games\n\n")
    nome = input("Digite o nome do game: ")
    console = input("Digite o console do game: ")
    genero = input("Digite o gênero do game: ")

    try:
        a = open("C:\Programacao\Portifolio\Facul\Logica de Programação e Algoritmos\Aula Pratica 4\colection.txt", "at")
    except Exception as e:
        print(f"Erro ao abrir arquivo: {e}")
    else:
        a.write(f"Game: {nome} | Console: {console} | Gênero: {genero}\n")
        a.close()

    print(f"\nGame '{nome}' cadastrado com sucesso!\n\n")


def listar_games():
    print("\n\nLista de Games Cadastrados\n")
    try:
        a = open("C:\Programacao\Portifolio\Facul\Logica de Programação e Algoritmos\Aula Pratica 4\colection.txt", "rt")
    except Exception as e:
        print(f"Erro ao abrir arquivo: {e}")
    else:
        for line in a:
            print(f"{line.strip()}\n")
    finally:
        a.close()