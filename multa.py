print("Parabéns você chegou ao rio de janeiro")
x = int(input("Radar de velocidade á frente. Quantos Km/h passou o carro |Limite 40km/h|:"))
if x >= 40:
    z = (x * 7) - (40 * 7)
    print("Você foi multado por exceder a velocidade, a Multa será de R${}".format(z))
else:
    print("Você passou á uma velocidade permitida !")
print("Bem vindo ao rio")

