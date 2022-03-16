def ficha(jog='', gol=''):
    if jog == '' and gol == '':
        jog = '<JOGADOR>'
        gol = 0
    if jog == '':
        jog = '<JOGADOR>'
    if gol.istitle():
        gol = 0
    if gol == '':
        gol = 0
    return print(f'O Jogador {jog} fez {gol} gols no campeonato')




nome = str(input('Digite o nome do jogador : '))
gols = str(input('Quantos gols o jogador fez na partida : '))
ficha(nome, gols)
