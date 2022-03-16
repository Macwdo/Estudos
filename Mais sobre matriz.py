matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somai = somat = valor2 = 0
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'Digite um valor para matriz na posição {c, l} :'))
        if matriz[c][l] % 2 == 0:
            somap += matriz[c][l]
        somat += matriz[2][l]
valor2 = max(matriz[1][0], matriz[1][1], matriz[1][1])
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print(f'A Soma dos valores pares da Matriz é {somap}')
print(f'A Soma de valores da Terceira coluna é {somat}')
print(f'O Maior valor da Segunda linha é {valor2}')
