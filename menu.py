import advinhacao
import forca

def menu_jogo():

    print("\n************************************")
    print("Jogos em Python. Escolha o seu jogo!")
    print("************************************")

    print("\n(1) Advinhação | (2) Forca")

    jogo = 0

# Lógica para seleção do jogo através do menu inicial.
# ====================================================

    while jogo != 1 and jogo != 2:
        jogo = int(input("Sua escolha: "))

        if (jogo == 1):
            print("Você escolheu o jogo de Advinhação.")
            advinhacao.jogar()
        elif (jogo == 2):
            print("Você escolheu o jogo da Forca.")
            forca.jogar()
        else:
            print("\nOpção inválida. Escolha o seu jogo!")
            print("(1) Advinhação | (2) Forca")

if(__name__ == "__main__"):
    menu_jogo()