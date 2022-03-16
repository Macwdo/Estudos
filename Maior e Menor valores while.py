sol = ""
n = s = cont = med = maior = menor = 0
while sol != "N":
    n = int(input("Digite um número:"))
    sol = str(input("Quer Continuar [S/N]")).upper().strip()[0]
    cont += 1
    s += n
    menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
med = s / cont
print(f"A Soma de tudo foi {s},a média foi {med:.2f}, Foram  {cont} Numéros digitados,"
      f", o maior foi {maior} e o menor foi {menor} ")
