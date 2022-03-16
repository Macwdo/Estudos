print('-=-=-' * 10)
print('                CAIXA ELETRONICO')
print('-=-=-' * 10)
valor = int(input('Digite o valor que você quer sacar : '))
valor50 = valor // 50
if valor50 > 0:
    print(f'Serão {valor50} notas de 50.')
valor = valor - valor50 * 50
valor20 = valor // 20
if valor20 > 0:
    print(f'Serão {valor20} notas de 20.')
valor = valor - valor20 * 20
valor10 = valor // 10
if valor10 > 0:
    print(f'Serão {valor10} notas de 10.')
valor = valor - valor10 * 10
valor5 = valor // 5
if valor5 > 0:
    print(f'Serão {valor5} notas de 5.')
valor = valor - valor5 * 5
valor1 = valor // 1
if valor1 > 0:
    print(f'Serão {valor1} notas de 1.')


