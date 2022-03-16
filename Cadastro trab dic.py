dados = {}
dados['Nome'] = str(input('Nome :'))
dados['Nascimento'] = int(input(f'Digite o Ano de nascimento de {dados["Nome"]} : '))
dados['Carteira'] = int(input(f'Número da Carteira de trabalho de {dados["Nome"]} [0 Para inexistente] : '))
if dados['Carteira'] != 0:
    dados['Ano de Contratação'] = int(input(f'Ano de contratação de {dados["Nome"]} : '))
    dados['Salario'] = int(input(f'Salario de {dados["Nome"]} : '))
else:
    print(f'{dados["Nome"]} não trabalha.')
print('-=-=-'*10)
idadet = dados['Ano de Contratação'] - dados['Nascimento']
dados['Aposentadoria'] = idadet + 30
dados['Dinheiro guardado'] = idadet * (12 * dados['Salario'] * 10/100)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')

