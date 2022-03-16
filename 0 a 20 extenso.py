numero = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
print('===' * 10)
print('   Leitor por extenso')
print('===' * 10)
while True:
    vr = int(input('Digite um numero de 0 a 10 : '))
    if 0 <= vr <= 10:
        print(f'o Numero digitado foi {numero[vr]}')
        cont = str(input('Deseja continuar [S/N]')).upper().strip()[0]
        if cont == 'S':
            pass
        if cont == 'N':
            break
    else:
        print('Digite um número valido')