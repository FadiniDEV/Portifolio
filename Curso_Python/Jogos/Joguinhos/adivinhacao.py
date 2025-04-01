import random

def jogar():

    print("\n\n*********************************")
    print("Bem vindo ao jogo do Adivinhão!")
    print("*********************************")
    numero_secreto = random.randrange(1, 21)
    total_de_tentativas = 3
    pontos = 50

    print("Vai Arregar??")
    print("Nivel: (1) Baitola (2) Tonto (3) Gostoso do krlh")

    nivel = int(input("\neai?\n"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 7
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("\nDigite um número entre 1 e 20: ")
        chute = int(chute_str)
        
        if(chute < 1 or chute > 20):
            print("DIGITA CERTO GARAIO!!")
            continue
        
        print("Você digitou " , chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("\nACERTO MISERAVI!!!\nE ainda por cima marcou {}/50 pontos".format(pontos))
            break
        else:
            if(maior):
                print("\nVAI COM CALMA KRAIO, o numero é menor\n")
            elif(menor):
                print("\nAUMENTA TUAS APOSTA!\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\n\nFim do Games :)")

if(__name__ == "__main__"):
    jogar()