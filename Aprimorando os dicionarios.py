gols = 0
pessoal = []
cont = 0
while True:
    dados = {'Nome':'','gols': []}
    dados['Nome'] = str(input('Digite o Nome do Jogador : ')).capitalize()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou : '))
    for c in range(0, partidas):
        gol = int(input(f'  Quantas gols {dados["Nome"]} fez na {c+1}ª  Partida:'))
        dados['gols'].append(gol)
        gols += gol
    dados['goltotal'] = gols
    pessoal.append(dados.copy())
    gols = 0
    dados.clear()
    while True:
        ir = str(input('Deseja continuar [S/N]')).upper().strip()[0]
        if ir == 'N':
            break
        elif ir == 'S':
            break
        else:
            print('Digite uma opção válida')
    if ir == 'N':
        break
print('=-=' * 20)
print('Cod Nome        Gols        total')
for k, v in enumerate(pessoal):
    print(f'{k:>3} ', end='')
    for c in v.values():
        print(f'{str(c)!s:<15}', end='')
    print()
print('=-=' * 20)
while True:
    sele = int(input('Mostrar dado de qual jogador : [999 Para!]'))
    if sele == 999:
        print('Finalizando')
        break
    elif sele > len(pessoal):
        print('Digite um valor valido')
    else:
        print(f'Levantamento do jogador {pessoal[sele]["Nome"]}')
        for i,g in enumerate(pessoal[sele]['gols']):
            print(f'No jogo {i+1} foram {g} gols')