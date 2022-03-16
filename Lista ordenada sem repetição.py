list  = []
for c in range(0, 5):
    k = int(input('Digite um número : '))
    if c == 0 or c > list[-1]:
        list.append(k)
    else:
        pos = 0
        while pos < len(list):
            if k <= list[pos]:
                list.insert(pos, k)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {list}')

