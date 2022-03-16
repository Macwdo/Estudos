num = []
for c in range(0,5):
    num.append(int(input('Digite um valor : ')))
print(f'O maior valor foi {max(num)} e ficou na posição {num.index(max(num)) + 1}º')
print(f'O menor valor foi {min(num)} e ficou na posição {num.index(min(num)) + 1}º')
