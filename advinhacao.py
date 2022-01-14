import random

print("\n*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000
nivel = 0

while nivel !=1 and nivel !=2 and nivel !=3:
    print("\nEscolha um nível de dificuldade:", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Sua escolha: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5
    else:
        print("Nível inválido. Escolha o nível de dificuldade desejada")

for rodada_atual in range(1, total_tentativas + 1):
    print("\n*********************************")
    print("Tentativa {} de {}".format(rodada_atual, total_tentativas))
    palpite = int(input("Escolha um número entre 1 e 100: "))

    if(palpite < 1 or palpite > 100):
        print("\nNúmero inválido! Você deve digitar um número entre 1 e 100!")
        continue

    correto  = palpite == numero_secreto
    maior = palpite > numero_secreto
    menor  = palpite < numero_secreto

    if(correto):
        print("\n*********************************")
        print("Parabéns, você acertou!")
        print("*********************************")
        break
    else:
        pontos_perdidos = abs(numero_secreto - palpite)
        pontos = pontos - pontos_perdidos
        if(maior):
            print("\nVocê errou! O número escolhido foi maior do que o número secreto.")
        elif(menor):
            print("\nVocê errou! O número escolhido foi menor do que o número secreto.")

    rodada_atual = rodada_atual + 1

print("\nFim do jogo.")
print("O número secreto era:", numero_secreto)
print("Sua pontuação foi de {} pontos".format(pontos))
print("\n*********************************")
