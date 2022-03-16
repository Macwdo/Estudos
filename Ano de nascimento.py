from datetime import date
an = int(input("Ano de nascimento:"))
atual = date.today().year
idd = atual - an
print("Quem Nasceu em {} tem {} anos.".format(an, idd))
if idd == 18:
    print("Está no ano de seu alistamento!".format(idd))
elif idd > 18:
    idp = atual - (idd - 18)
    print("Ja passou o ano de se alistar. O Ano de seu alistamento era {}".format(idp))
elif idd < 18:
    idf = 18 - idd
    idn = 2022 + idf
    print("Faltam {} anos para o seu alistamento que será no ano de {}".format(idf, idn))
