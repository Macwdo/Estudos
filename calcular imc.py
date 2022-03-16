print("Vamos calcular seu imc")
alt = float(input("Digite sua altura em no formato x.xx:"))
pes = int(input("Digite seu peso em kg:"))
imc = pes / (alt ** 2)
print("Seu imc é de {:.1f} ".format(imc))
if imc < 18.5:
    print("Você está abaixo do peso:")
elif 18.5 <= imc < 25:
    print("Você está no peso ideal")
elif 25 <= imc < 30:
    print("Você está com sobrepeso")
elif 30 <= imc < 40:
    print("Você está Obeso")
elif imc > 40:
    print("Você está com obesidade mórbida")
