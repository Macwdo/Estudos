# nome sexo idade media de idade mais velho homem idade , mulheres menor que 20
idh = 0
idm = 0
si = 0
idhm = ""
for c in range(1, 5):
    print("{} Pessoa".format(c))
    nm = str(input("Nome da {}ª pessoa:".format(c)))
    sx = str(input("Sexo da {}ª pessoa [M/F]".format(c))).upper()
    id = int(input("Idade da {}ª pessoa:".format(c)))
    si = si + id
    if sx == "M":
        if id > idh:
            idh = id
            idhm = nm
    elif sx == "F":
        if id < 20:
            idm += 1
mid = si / 4
if idm > 1:
    print \
        ("""O Homem mais velho é {},
    A media de idade do grupo é {:.2f},
    Há {} mulheres com menos de 20 anos"""
         .format(idhm, mid, idm))
else:
    print \
        ("""O Homem mais velho é {} com {} anos,
    A media de idade do grupo é {:.2f},
    Há apenas {} mulher com menos de 20 anos"""
         .format(idhm, idh, mid, idm))
