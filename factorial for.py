num = int(input("Digite um Numero:"))
nf = num
f = 1
for nf in range(num,0,-1):
    print("{}".format(nf),end="")
    print(" x " if nf > 1 else " = ", end="")
    f = nf * f
print("O Fatorial de {} é {}".format(num, f))
