num = int(input("Digite um Número:"))
f = num
c = 1
print("Calculando {}!".format(num))
while f > 0:
    print("{}".format(f), end ="")
    print(" x "if f > 1 else " = ", end ="")
    c = c * f
    f -= 1
print("o Fatorial é {}".format(c))