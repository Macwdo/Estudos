import random
from random import randint
x = randint(0, 10)
acertou = False
vqt = 0
while not acertou:
    jogador = int(input("Digite um valor:"))
    vqt += 1
    if x == jogador:
        acertou = True
        if vqt > 5:
            print("Você perdeu")
        else:
            print("Você Ganhou")
    else:
        if x > jogador:
            print("Mais pra cima...")
        else:
            print("Mais pra baixo...")
print("Você acertou tentando {} vezes!!! Eu Pensei no {}.".format(vqt, x))
print(x)