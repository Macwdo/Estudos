print("\33[1;30m -=-=-" * 10)
print("\33[1;38m                      Seja bem vindo\33[0;m")
print("\33[1;30m -=-=-" * 10)
vdc = float(input("\33[1;33m Qual valor do emprestimo para compra da casa:\33[0m"))
sdc = float(input("\33[1;33m Qual o seu salário:"))
qpg = int(input(" Em Quantos anos vai pagar?"))
#parcela no total
pnt = qpg * 12
#preço divido
pd = vdc / pnt
#pagamento mensal
pm = sdc * (30/100)
if pd > pm:
    print("\33[1;32m Desculpe você não poderá efetuar o emprestimo.")
    print("O Valor das parcelas mensalmente ficaria em {:.2f}".format(pd))
else:
    print("\33[1;32m Emprestimo aprovado parabéns pela casa!!!")
    print("O Valor das parcelas mensalmente ficará em {:.2f}".format(pd))
print("Boa noite!!!")



