lista = []
dado = []
while True:
    nome = str(input('Digite o Nome : ')).capitalize()
    nota1 = int(input('Digite a 1º Nota : '))
    nota2 = int(input('Digite a 2º Nota : '))
    dado.append(nome)
    dado.append(nota1)
    dado.append(nota2)
    media = (dado[1] + dado[2]) / 2
    dado.append(media)
    lista.append(dado[:])
    dado.clear()
    cont = str(input('Quer Continuar [S/N]')).upper().strip()[0]
    while cont not in 'SsNn':
        cont = str(input('Quer Continuar [S/N]')).upper().strip()[0]
        if cont in 'Nn':
            cont = 'N'
            break
    if cont in 'N':
        break

print('-=-' * 10)
print('Nº |   Nome   | média |')
for n, n1 in enumerate(lista):
    print(f'{n:<5} {n1[0]:<10} {n1[3]:.1f}')
print('-=-' * 10)
while True:
    stop = int(input('Deseja ver a nota de qual aluno [Stop -> 999]: '))
    if stop == 999:
        print('Fim do programa')
        break
    if stop <= len(lista) -1:
        print(f'Notas de {lista[stop][0]} são {lista[stop][1],lista[stop][2]}')