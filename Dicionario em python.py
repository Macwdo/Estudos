dicio = {}
dicio['Nome'] = str(input('Digite o Nome do aluno :')).capitalize()
dicio['Nota'] = int(input(f'Nota de {dicio["Nome"]} '))
print('*--*'*20)
if dicio['Nota'] >= 7:
    dicio['Situação'] = 'Aprovado'
elif dicio['Nota'] >= 4:
    dicio['Situação'] = 'Recuperção'
else:
    dicio['Situação'] = 'Reprovado'
for k,v in dicio.items():
    print(f'{k} é {v}')