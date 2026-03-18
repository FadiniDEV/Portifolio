cadastro = {"nome": [], "idade": [], "sexo": []}

while True:
    terminar = input("Deseja cadastrar uma pessoa? (s/n) ")
    if terminar.lower() == 'n':
        break
    if terminar.lower() == 's':
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ")
        
        cadastro["nome"].append(nome)
        cadastro["idade"].append(idade)
        cadastro["sexo"].append(sexo)

visualizar = input("Deseja visualizar todos os cadastros? (s/n) ")

if visualizar.lower() == 's':
    print("\nCadastro completo:\n")
    for i in range(len(cadastro["nome"])):
        print(f"Nome: {cadastro['nome'][i]}\nIdade: {cadastro['idade'][i]}\nSexo: {cadastro['sexo'][i]}\n")

    print(f"Total de pessoas cadastradas: {len(cadastro['nome'])}")
    print(f"Total de mulheres com menos de 30 anos: {sum(1 for i in range(len(cadastro['nome'])) if cadastro['sexo'][i].upper() == 'F' and cadastro['idade'][i] < 30)}")
    print(f"Média de idades das pessoas cadastradas: {sum(cadastro['idade']) / len(cadastro['idade']) if cadastro['idade'] else 0:.2f}")
    print(f"Lista de homens com idade acima da média:\n{[cadastro['nome'][i] for i in range(len(cadastro['nome'])) if cadastro['sexo'][i].upper() == 'M' and cadastro['idade'][i] > (sum(cadastro['idade']) /
    len(cadastro['idade']) if cadastro['idade'] else 0)]}")

else:
    print("Encerrando o programa...")
