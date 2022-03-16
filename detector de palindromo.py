fr = str(input("Digite uma frase")).upper().strip()
frs = fr.split()
xj = "".join(frs)
inverso = ""
for c in range(len(xj) - 1, -1, -1):
    inverso += xj[c]
print("O inverso é {}".format(inverso))
if inverso == xj:
    print("È palindromo")
else:
    print("Não é palindromo")