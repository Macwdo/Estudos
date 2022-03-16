x = int(input("Quantos alunos tem na sala:"))
mn = 0
mal = ""
for c in range(1, x+1):
    np = str(input("Qual nome do {}ª aluno:".format(c)))
    nt = int(input("Qual a nota do {}ª aluno:".format(c)))
    print("-"* 10)
    if nt > mn:
        mn = nt
        mal = np

print("A Maior nota foi {} de {}".format(mn,mal.capitalize()))
