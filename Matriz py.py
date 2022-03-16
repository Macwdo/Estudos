matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição {l,c}: '))
print('-=-'*20)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^5}]',end='')
    print()