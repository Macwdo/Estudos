maioridd = 0
homens = 0
mmenoridd = 0
sexo = ' '
while True:
    idade = int(input('Digite a idade da pessoa : '))
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo [M/F]')).upper().strip()[0]
        if idade >= 18:
            maioridd += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F':
            if idade < 20:
                mmenoridd += 1
    pros = str(input('Quer prosseguir com o programa : [S/N] ')).strip().upper()[0]
    if pros == 'N':
         break
print(f'Existem {maioridd} pessoas maiores de 18 anos. ')
print(f' Existem um total de {homens} homens cadastrados.  ')
print( f' Existem um total de {mmenoridd} mulheres menores de 20 anos.')



