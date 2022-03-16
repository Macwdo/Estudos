lis = []
while True:
    k = (int(input('Digite um Numero para adicionar na lista : ')))
    if k == 999:
        break
    if k not in lis:
        lis.append(k)
        print('Valor adicionado')
    else:
        print('Valor duplicado nao será adicionado')
print(lis)
print(sorted(lis))