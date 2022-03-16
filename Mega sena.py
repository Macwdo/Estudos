from random import randint


def linha():
    print('-' * 20)

linha()
print('     MEGA SENA')
linha()
qtd = int(input('Quantas bilhetes você quer jogar : '))
for jg in range(0, qtd):
    lista = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    lista.sort()
    print(f'O resultado do jogo {jg+1} é : {lista}')

