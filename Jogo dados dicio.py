import random
from time import sleep
from operator import itemgetter
dados = {}
ranking = []
print('-=-'*20)
print('                        --Jogadas--')
print('-=-'*20)

for c in range(0,4):
    dados[f'Jogador{c+1}'] = random.randint(0,6)
    print(f'Jogador{c+1} jogou {dados[f"Jogador{c+1}"]}')
    sleep(0.5)
print('-=-'*20)
print('               --Ranking Dos Jogadores--')
print('-=-'*20)
ranking = sorted(dados.items(), key=itemgetter(1),reverse=True)
sleep(0.5)

for jo, ja in enumerate(ranking):
    print(f'    {jo+1} lugar : {ja[0]} com {ja[1]} ')
    sleep(0.5)
