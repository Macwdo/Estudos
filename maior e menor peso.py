mp = 0
mnp = 0
s = 0
for c in range(1,6):
    x = int(input("Digite o peso da {}ª pessoa ".format(c)))
    if x > mp:
        mp = x
    else:
        mnp = x
print("O Maior peso foi {} e o menor peso foi {}".format(mp,mnp))