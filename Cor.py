print("\33[4;32m Olá mundo \33[0;m")
nome = str(input("\33[1;34mQual é seu nome?"))
x = nome.capitalize()
if x == "Danilo":
    print("{}{}{}\33[1;34m nome de quem transa!".format("\33[4;35m", x, "\33[0;m"))
elif x in " Cauã Jhonny Moisés":
    print("\33[1;34m Virgem eterno")
elif x == "Daniel":
    print("\33[1;35m Nome de quem senta na banana\33[0;m")
elif x in "Daniella Sandra ":
    print("\33[1;35m Nome de Femêa gorda")
else:
    print("\33[1;36m Você não é digno do sexo")
print("\33[1;32m Tenha um bom dia {}{}{}".format("\33[4;35m", x, "\33[0;m"))