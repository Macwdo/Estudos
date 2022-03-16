x1 = int(input("\33[1:38mPrimeiro valor:"))
x2 = int(input("\33[1:38mSegundo valor:"))
x = 0

while x != 5:
    x = int(input("""
\33[4:1:32mMenu de opções\33[0m\33[1:36m
[1]Somar
[2]Multiplicar
[3]Maior Número
[4]Novos Números
[5]Sair do Programa \33[1:32m
Digite a opção:\33[0m"""))
    if x == 1:
        x = x1 + x2
        print("\33[1:38mA Soma é {}".format(x))
    elif x == 2:
        x = x1 * x2
        print("\33[1:38mO Produto é {}".format(x))
    elif x == 3:
        if x1 > x2:
            print("\33[1:38mO Maior é {}".format(x1))
        elif x1 < x2:
            print("\33[1:38mO Maior é {}".format(x2))
        else:
            print("\33[1:38mSão iguais.")
    elif x == 4:
        print("\33[1:38mOk Digite os Novos Números.")
        x1 = int(input("\33[1:38mPrimeiro valor:"))
        x2 = int(input("\33[1:38mSegundo valor:"))

    elif x == 5:
        print("\33[1:38mFim do programa!")
print("\33[1:32mObrigado por usar o programa do sexo, Volte sempre!!!")