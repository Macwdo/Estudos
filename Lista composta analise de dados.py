temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Ao todo você registrou {len(princ)} pessoas')
print(f'O Maior peso foi de {maior}kg.Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]')
print(f'O Menor peso foi  de {menor}kg.Peso de ',end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]')

