from random import randint
contadorv = 0
while True:
    jogador_num = int(input('Digite um Número: '))
    maquina_num = randint(1, 10)
    soma = int(maquina_num + jogador_num)
    jogador_esc = ' '
    while jogador_esc not in 'PpIi':
        jogador_esc = str(input('Você quer [I]mpar ou [P]ar :').upper().strip()[0])
    if jogador_esc == 'I':
        jogador_esc = 'Impar'
        if soma % 2 != 0:
            print(f'Você ganhou!!! sua escolha foi {jogador_esc} e o resultado foi {soma}.')
            contadorv += 1
            print(f'{contadorv} vitorias consecutivas')
        else:
            print(f'Você perdeu!!! sua escolha foi {jogador_esc} e deu par . O resultado foi {soma}')
            print(f'Você perdeu. Conseguiu {contadorv} vez')
            break
    if jogador_esc == 'P':
        jogador_esc = 'Par'
        if soma % 2 == 0:
            print(f'Você ganhou, sua escolha foi {jogador_esc} e o resultado foi {soma}')
            contadorv += 1
            print(f'{contadorv} vitorias consecutivas')
        else:
            print(f'Você perdeu!!! sua escolha foi {jogador_esc} e deu impar . O resultado foi {soma}')
            print(f'Você perdeu. Conseguiu {contadorv} vez')
            break


