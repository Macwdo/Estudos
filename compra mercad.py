print("Bem vindo ao mercado do sexo")
vlr = int(input("Qual o valor da Compra"))
print("""Qual a forma de pagamento
[1] A Vista no Dinheiro ou Cheque
[2] A Vista no Cartão
[3] 2 vezes no Cartão
[4] 3 vezes ou mais no Cartão""")
fmp = int(input("Digite a forma de pagamento"))
vcc = vlr - vlr * (5/100)
vc = vlr - vlr * (10/100)
if fmp == 1:
    print("O Valor final da compra no dinheiro ou cheque com desconto foi de : R${}".format(vc))
elif fmp == 2:
     print("O Valor final da compra no cartão a vista foi de : R${}".format(vcc))
elif fmp == 3:
     print("O Valor final das 2 parcelas no cartão será de : R${:.2f}".format(vlr / 2))
elif fmp == 4:
    xz = int(input("Quantas vezes no cartão?"))
    vt = vlr + (vlr * 20/100)
    vfcd = vt / xz
    print("O total será de {} e o Valor de cada parcela no cartão será de : R${:.2f}".format(vt, vfcd))
else:
    print("Opção invalida tente novamente.")
print("Sua compra vai custar R$", vlr, "no final" )


