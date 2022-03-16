print("-=-" * 10)
print("Convertor de moedas")
print("-=-" * 10)
qvc = int(input("Quantas vezes quer fazer uma conversão de moeda:"))
dl = 5.33
mvl = 0
mvls = 0
s = 0
for c in range(1, qvc+1):
    qdv = int(input("{}ª valor:".format(c)))
    if qdv > mvl:
        mvl = qdv / dl
    else:
        mvls = qdv
        mvls = qdv / dl
    qdv = qdv / dl
    print("{:.2f}".format(qdv))
    s = qdv + s
print("A Soma é {:.2f}".format(s))
print("O Maior valor foi {:.2f} e menor foi {:.2f}".format(mvl,mvls))

