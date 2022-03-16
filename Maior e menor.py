print("Vamos ver qual é maior e menor. Digite 3 numeros")
x1 = int(input("Número 1:"))
x2 = int(input("Número 2:"))
x3 = int(input("Número 3:"))
if x2 < x1 > x3:
    print("O {} é o maior".format(x1))
if x1 < x2 > x3:
    print("O {} é o maior".format(x2))
if x1 < x3 > x2:
    print("O {} é o maior".format(x3))
if x2 > x1 < x3:
    print(" O {} é o menor".format(x1))
if x1 > x2 < x3:
    print("O {} é o menor".format(x2))
if x1 > x3 < x2:
    print("O {} é o menor".format(x3))

