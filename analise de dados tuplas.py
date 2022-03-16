n1 = int(input('Digite um valor :'))
n2 = int(input('Digite outro valor :'))
n3 = int(input('Digite mais um valor :'))
n4 = int(input('DIgite o Ultimo valor :'))
tpl = (n1, n2, n3, n4)
v9 = tpl.count(9)
count = 0
if tpl.count(9) == 0:
    print('O valor 9 não foi digitado na tupla')
else:
    if tpl.count(9) == 1:
        print(f'Apareceu {v9} vez o numero 9 na tupla ')
    else:
        print(f'Apareceu {v9} vezes o numero 9 na tupla')
if tpl.count(3) == 0:
    print('O Valor 3 não foi digitado na tupla')
else:
    print(f'O Primeiro valor 3 ficou na posição {tpl.index(3) + 1}')
for p in tpl:
    if p % 2 == 0:
        if p != 0:
            count += 1
print(f'Existem {count} pares na lista')

