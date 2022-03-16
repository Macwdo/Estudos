def maiordef(*num):
    cont = 0
    maior = 0
    print('-' * 20)
    print('Analisando todos valores ao todo')
    totnum = list(num)
    for tot in totnum:
        print(f'{tot}', end=' ')
        if cont == maior:
            maior = tot
        else:
            if tot > maior:
                maior = tot
        cont += 1
    print(f'foram informados {cont} numeros, o maior foi {maior}')


maiordef(4, 43, 2, 1, 2, 2, 2, 3, 4)
