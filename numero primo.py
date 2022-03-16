x = int(input("Digite o numero:"))
tot = 0
for c in range(1, x+1):
    if x % c == 0:
        print("\033[1;33m", end="")
        tot += 1
    else:
        print("\33[1;34m", end="")
    print("{}".format(c), end="")
print("\33[37m O Numero {} foi divisível {} vezes".format(x, tot))
if tot == 2:
    print("è primo")
else:
    print("Não é primo")