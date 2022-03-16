dados = {'gols':[]}
gols = 0
dados['Nome'] = str(input('Digite o Nome do jogador: '))
dados['Partidas'] =  int(input(f'Quantas partidas {dados["Nome"]} jogou :'))
print('-=-' * 10)
for g in range(0, dados['Partidas']):
    gol = int(input(f'Quantos gols {dados["Nome"]} fez {g+1}º partida : '))
    gols += gol
    dados['gols'].append(gol)
print('-=-' * 10)
for k, v in dados.items():
    print(f'o Campo {k} tem o valor {v}')
print('-=-' * 10)
print(f'O Jogador {dados["Nome"]} jogou {dados["Partidas"]}.')
for partida,golst in enumerate(dados['gols']):
    print(f'Na Partida {partida + 1} , fez {golst} gols')
print(f'{dados["Nome"]} fez um total de {gols} gols')



