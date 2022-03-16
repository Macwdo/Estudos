import random
print("Ola mundo.")
#fazer pensar em um numero
x = random.randint(1, 5)
z = int(input("Digite um numero"))
if x == z:
    print("Numero correto. O numero escolhido foi {}".format(x))
    print("Você ganhou!!!")
else:
    print("Tente outra vez o numero certo era {}".format(x))
    print("Você perdeu")

