lop = []
cont = ''
while True:
    k = int(input('Digite um valor :'))
    if k not in lop:
        lop.append(k)
        lop.sort(reverse=True)
    else:
        print('Numero ja existente na lista, Não será inserido.')
    cont = str(input('Deseja continuar [S/N]')).upper().split()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]')).upper().split()[0]
        if cont == 'N':
            cont = 'N'
            break
        elif cont == 'S':
            break
    if cont == 'N':
        break
if 5 not in lop:
   print('O Número 5 nao foi encontrado na lista')
else:
   print(f'O Número 5 está na {lop.index(5)+1} posição')
print(f'Você digitou {len(lop)} elementos. ')
print(f'Em ordem decrescente a lista fica assim {lop}')
