def fatorial(num, show=True):
    """Calculo fatorial de um numero
       :param num: Numero a ser calculado
       :param show: Mostrar ou não a conta
       :return: O valor fatorial de um Numero N"""



    f = 1
    print('---' * 15)
    if show:
        for c in range(num, 1, -1):
            f *= c
            print(f' {c} ', end='x')
        print(f' 1 =', end=' ')

        return f
    else:
        for c in range(num, 1, -1):
            f *= c
        return f


print('---'*15)


help(fatorial)
n = int(input('Digite um número : '))


while True:
    op = str(input('Deseja mostrar o resultado [S/N]')).upper().strip()[0]
    if op == 'S':
        op = True
        break
    elif op == 'N':
        op = False
        break
    else:
        print(f'Digite uma opção valida')
print(f'{fatorial(n,op)}')

