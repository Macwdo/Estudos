import time


def contador(i, f, p):
    print('-=-' * 10)
    print(f'Contagem de {i} até {f} pulando de {p} em {p} ->',end=' ')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        for c in range(i, f, p):
            print(f'{c}', end=' ')
            time.sleep(0.5)
        print('Fim')
        print('-=-' * 10)
    else:
        p = -p
        for c in range(i, f, p):
            print(f'{c}', end=' ')
            time.sleep(0.5)
        print('Fim')
        print('-=-' * 10)


Inicio = int(input('Onde vai começar a contagem :'))
Fim = int(input('Fim da contagem :'))
Passo = int(input('Passo da contagem :'))
contador(0,10,1)
contador(0,10,2)
contador(Inicio, Fim , Passo)

