print("Bem vindo ao calculador de preços de pizzas do Lucas Fadini Apolinário!")

#Laço de repetição para exibir o menu
while True:
    print("\n\n", 5 * "*", "Menu", 5 * "*","\n")
    print("1 - Retirar pizza")
    print("2 - Sair\n")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:

        print("\n", " " * 15, 5 * "*", "Cardapio", 5 * "*", "\n")

        print("-" * 56)
        print("-" * 5, "Tamanho", "-" * 5, "Pizza Doce", "-" * 5, "Pizza Salgada", "-" * 5)
        print("-" * 8, "P", "-" * 9, "R$ 34,00", "-" * 8, "R$ 30,00", "-" * 8)
        print("-" * 8, "M", "-" * 9, "R$ 48,00", "-" * 8, "R$ 45,00", "-" * 8)
        print("-" * 8, "G", "-" * 9, "R$ 66,00", "-" * 8, "R$ 60,00", "-" * 8)
        print("-" * 56)

        #definindo a variavel total para a execução do programa
        total = int(0)

        #Laço de repetição para somar quais pizzas o cliente deseja retirar e mostrar o valor total da compra
        while True:

            sabor = input("\n\nQual sabor de pizza você deseja?\nPD - Pizza Doce\nPS - Pizza Salgada\n")

            #IF para escolha das pizzas doces e seus tamanhos
            if sabor.upper() == "PD":

                tamanho = input("\n\nQual o tamanho da pizza?\nP - Pequena\nM - Média\nG - Grande\n")

                if tamanho.upper() == "P":
                    
                    qtd = int(input("\n\nQuantas pizzas doce pequena você deseja? "))
                    total += (qtd * 34)

                    continuar = input("\nDeseja retirar mais pizzas? (S/N) ")

                    if continuar.upper() == "S":
                        print("\nO que mais deseja?\n")
                        continue
                    else:
                        print("\nObrigado por usar o calculador de preços!\n")
                        break

                elif tamanho.upper() == "M":

                    qtd = int(input("\n\nQuantas pizzas doce média você deseja? "))
                    total += (qtd * 48)

                    continuar = input("\nDeseja retirar mais pizzas? (S/N) ")

                    if continuar.upper() == "S":
                        print("\nO que mais deseja?\n")
                        continue
                    else:
                        print("\nObrigado por usar o calculador de preços!\n")
                        break

                elif tamanho.upper() == "G":

                    qtd = int(input("\n\nQuantas pizzas doce grande você deseja? "))
                    total += (qtd * 66)
                    
                    continuar = input("\nDeseja retirar mais pizzas? (S/N) ")

                    if continuar.upper() == "S":
                        print("\nO que mais deseja?\n")
                        continue
                    else:
                        print("\nObrigado por usar o calculador de preços!\n")
                        break

                else:
                    print("\nTamanho inválido! Tente novamente.\n")
                    continue

            #Elif para pizzas salgadas e seus tamanhos
            elif sabor.upper() == "PS":

                tamanho = input("\n\nQual o tamanho da pizza?\nP - Pequena\nM - Média\nG - Grande\n")

                if tamanho.upper() == "P":

                    qtd = int(input("\n\nQuantas pizzas salgada pequena você deseja? "))
                    total += (qtd * 30)
                    
                    continuar = input("\nDeseja retirar mais pizzas? (S/N) ")

                    if continuar.upper() == "S":
                        print("\nO que mais deseja?\n")
                        continue
                    else:
                        print("\nObrigado por usar o calculador de preços!\n")
                        break

                elif tamanho.upper() == "M":

                    qtd = int(input("\n\nQuantas pizzas salgada média você deseja? "))
                    total += (qtd * 45)
                    
                    continuar = input("\nDeseja retirar mais pizzas? (S/N) ")

                    if continuar.upper() == "S":
                        print("\nO que mais deseja?\n")
                        continue
                    else:
                        print("\nObrigado por usar o calculador de preços!\n")
                        break

                elif tamanho.upper() == "G":

                    qtd = int(input("\n\nQuantas pizzas salgada grande você deseja? "))
                    total += (qtd * 60)
                    
                    continuar = input("\nDeseja retirar mais pizzas? (S/N) ")

                    if continuar.upper() == "S":
                        print("\nO que mais deseja?\n")
                        continue
                    else:
                        print("\nObrigado por usar o calculador de preços!\n")
                        break

                else:
                    print("\nTamanho inválido! Tente novamente.\n")
                    continue

            #Else para bloquear qualquer tipo de entrada que não seja PS ou PD e voltar ao começo do laço
            else:
                print("\nSabor inválido! Tente novamente.\n")
                continue
            
        #Print do valor total somado apos o laço se encerar
        print(f"\nO valor total da sua compra é de R$ {total:.2f}\n")
        break

    #Opção para encerrar o programa caso o cliente queira
    elif opcao == 2:
        print("\nObrigado por usar o calculador de preços!\n")
        break
    
    #Filtro para as escolhas 1 e 2 somente
    else:
        print("\nDigite uma opção valida!\n")