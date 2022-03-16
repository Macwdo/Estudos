lopi = []
lopp = []
cont = ''
while True:
    k = int(input('Digite um Número : '))
    if k % 2 == 0:
        lopp.append(k)
    else:
        lopi.append(k)
    lopc = lopi + lopp
    cont = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]')).upper().strip()[0]
        if cont == 'N':
            cont = 'N'
            break
    if cont in 'N':
        break
print(f'A Lista completa é {lopc}')
print(f'A Lista dos impares é {lopi}')
print(f'A lista dos Pares é {lopp}')