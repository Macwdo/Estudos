tup = ('Lapís' ,1.33
       , 'borracha' ,1.99
       , 'estojo' ,7.99 ,
       'caneta' ,2.19 ,
       'apontador' ,4.95 ,
       'regua' ,9.39 ,
       'tesoura' ,10.99 ,
       'tinta' ,2.99 )
print('       Lista de preço')
for c in range(0,len(tup)):
       if c % 2 == 0:
              print(f'{tup[c]:.<30}',end='')
       else:
              print(f'R$ {tup[c]}')