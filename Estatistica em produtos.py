soma = 0
pros = ' '
mmil = 0
mbrt = 0
mbrtn = ' '
while True:
    nome_produto = str(input('Qual o Produto você deseja registar : '))
    preco_produto = int(input('Qual preço do produto registrado : R$ '))
    soma += preco_produto
    mbrt = preco_produto
    mbrtn = nome_produto
    if preco_produto > 1000:
        mmil += 1
    if preco_produto < mbrt:
        mbrt = preco_produto
        mbrtn = nome_produto
    pros = str(input('Deseja continuar [S/N]')).upper().strip()
    if pros == 'N':
        break
print(f' O Total gasto na compra foi R$ {soma}')
print(f' Foram {mmil} Produto(s) que custaram mais de R$1000')
print(f' O Produto mais barato foi a {mbrtn} custando apenas R${mbrt}')
