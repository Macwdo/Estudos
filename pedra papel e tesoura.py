import random
import time
print("""Diga qual você Escolhe:
[0] Pedra
[1] Papel
[2] Tesoura""")
x = int(input("Qual a sua escolha:"))
z = ["Pedra","Papel","Tesoura"]
y = random.choice(z)
if y == z[1] and x == 2:
    print("Você ganhou da Máquina ela escolheu {} e você {}".format(y, z[2]))
elif y == z[0] and x == 1:
    print("Você ganhou da Máquina ela escolheu {} e você {}".format(y, z[1]))
elif y == z[2] and x == 0:
    print("Você ganhou da Máquina ela escolheu {} e você {}".format(y, z[0]))
elif y == z[0] and x == 0:
    print("Empate , escolhas iguais. Tente novamente!!!")
elif y == z[1] and x == 1:
    print("Empate , escolhas iguais. Tente novamente!!!")
elif y == z[2] and x == 2:
    print("Empate , escolhas iguais. Tente novamente!!!")
else:
     print("Você perdeu a maquina escolheu {} tente novamente!!!".format(y))
print("Escolha da Maquina: {}".format(y))
if x == 0:
    x = "Pedra"
elif x == 1:
    x = "Papel"
elif x == 2:
    x = "Tesoura"
print("Sua Escolha: {}".format(x))









#z[0]pedra z[1]papel z[2]tesoura