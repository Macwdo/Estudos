def voto(idade):
    idp = 2022 - idade
    if 65 > idp >= 18:
        print(f'Com {idp} anos : Voto obrigatorio ')
    elif 18 > idp >= 16 or idp >= 65:
        print(f'Com {idp} anos : Voto Opcional')
    else:
        print(f'Com {idp} anos : Não vota')


nasc = int(input('Digite o seu ano de nascimento : '))
voto(nasc)
