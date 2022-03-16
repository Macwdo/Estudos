def textoal(text):
    numc = len(text) #Numero de caracteres
    print('=' * (numc + 2))
    print(f'{text: ^{numc+2}}')
    print('=' * (numc + 2))

frase = str(input('Digite um texto : '))
textoal(frase)