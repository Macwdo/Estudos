from time import sleep
print("\33[1;38m-=-=-" * 10)
print("\33[1;36m              |  Cutting ou Bulking  |\33[1;38m")
print("\33[1;38m              |     Bem vindo!!!     |")
print("-=-=-" * 10)
print("Vamos começar?")
sleep(1)
#1.nome
nome = str(input("Qual seu Nome:")).capitalize()
print("Bom dia {}".format(nome))
#2.Sex
sex = str(input("Qual seu Sexo [Masculino/Feminino]")).strip().upper()
sex = sex[0]
#3.idade
idd = int(input("Qual sua idade {} :".format(nome)))
if idd > 40:
    print("Você ja está velho {}.")
elif idd < 18:
    print("Ah, Adolescência, Que boa fase! ")
elif idd < 12:
    if sex == "F":
     print("Você é bem novinha {}".format(nome))
    elif sex == "M":
        print("Você é bem novinho {}".format(nome))
#4.altura
alt = int(input("Me diga sua Altura em cm Ex:\33[1;37m  |173cm| :"))
if alt > 183:
    if sex == "F":
        print("Você é uma Dinossaura {}")
elif alt < 160:
    if idd > 17:
        if sex == "M":
            print("Nossa , você é bem baixo {}".format(nome))
elif alt > 200:
    print("Fofoca!")

#5.prntImc
#6.prntbasal
##1.inpt(Bulk) supravt 500+
#1.1.macCarb 33%total
#1.2.macProt  2.0/g k
#1.3macGord
#2.inpt(cutt) defct 500-
#2.1macCarb 5/kg+
#2.2macProt 1,6/kg+
#2.3macGord 0,25/kg+