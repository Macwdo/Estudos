n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
nm = (n1 + n2) / 2
if nm < 6:
    print("O aluno está em recuperação pois não atingiu a média")
else:
    print("O aluno atingiu a média")
print(" A Média do aluno foi {} em base sua primeira {} e segunda {} nota".format(nm, n1, n2))
