n1 = int(input("\33[1;34m Primeiro numero:\33[0;m"))
n2 = int(input("\33[1;34m Segundo numero:\33[0;m"))
if n1 > n2:
    print("{}{}{} \33[1;33m é Maior que \33[0;m {}{}".format("\33[1;34m", n1, "\33[1;35m","\33[1;34m", n2))
elif n1 < n2:
    print("{}{}{} \33[1;33m é Maior que \33[0;m {}{}".format("\33[1;34m", n2, "\33[1;35m","\33[1;34m", n1))
else:
    print("{}{}{} é igual á {}{}".format("\33[1;34m", n2, "\33[1;35m","\33[1;34m", n1))
