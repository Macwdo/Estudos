lista = [[], []]

for tot in range(1,8):
    k = (int(input(f'Digite o {tot}º valor : ')))
    if k % 2 == 0:
        lista[0].append(k)
    else:
        lista[1].append(k)
lista[1].sort()
lista[0].sort()
print(f'Os valores impares foram {lista[1]}\n'
      f'Os valorees Pares foram {lista[0]}')


