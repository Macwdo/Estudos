def calcarea(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno {largura}m x {comprimento}m é igual a {area}m²')
print('              Controle de terrenos')
print('-=-' * 18)
largura = float(input('Digite a largura do terreno (m) : '))
comprimento = float(input('Digite o comprimento do terreno (m) : '))
calcarea(largura,comprimento)