print("_-_" * 10)
print("\33[1;34m          Super P.A\33[0m")
print("_-_" * 10)
pt = int(input("Digite o Primeiro termo:"))
rz = int(input("Digite a Razão:"))
termo = pt
c = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
            print("{}".format(termo), end=">")
            termo += rz
            c += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais você q  uer mostrar:"))
print("Apareceram um total de {} termos".format(c))
print("Fim")