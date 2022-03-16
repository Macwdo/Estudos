print("\033[4;35mOla mundo")
x = int(input("\033[1;37;40mDigite um ano e vamos ver se ele é bissexto:"))
if x % 4 == 0:
    print("{} é um ano bissexto".format(x))
else:
    print("{} não é um ano bissexto".format(x))
