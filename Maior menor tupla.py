import random

num = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
print(f'Os numeros sorteados foram {num}')
num = sorted(num)
print(num)
print(f'O Menor valor é {min(num)}')
print(f'O Maior valor é {max(num)}')

