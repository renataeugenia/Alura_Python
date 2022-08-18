import random

def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de Adivinhação!!!")
    print("***********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print(" Qual o nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Informe o nível:  "))
    if nivel == 1:
        total_tentativas = 10
    elif nivel == 2:
        total_tentativas = 5
    else:
        total_tentativas = 3

    for rodada in range(1, total_tentativas +1):
        print("Tentativa {} de {} " .format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100 : ")
        print("Voce digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Voce deve digitar um número entre 1 e 100!")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if acertou:

            print("Voce acertou!!! e fez {} pontos! " .format(pontos))
            break

        else:
            if maior:

                print(" Voce errou! O seu chute foi Maior que o numero secreto...")
                if rodada == total_tentativas:
                    print("O numero secreto era {} . Voce fez {} ".format(numero_secreto, pontos))
            elif menor:

                print(" Voce errou! O seu chute foi Menor que o numero secreto...")
                if rodada == total_tentativas:
                    print("O numero secreto era {} . Voce fez {} ".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if  __name__=="__main__":
    jogar()

