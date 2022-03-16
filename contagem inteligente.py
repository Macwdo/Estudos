print("Contagem inteligente")
print("=-" * 10)
inc = int(input("Inicio:"))
fim = int(input("Fim:"))
if inc > fim:
    for c in range(inc,fim-1,-1):
        print("{}".format(c), end=",")
else:
    for c in range(inc,fim+1):
        print("{}".format(c), end=",")