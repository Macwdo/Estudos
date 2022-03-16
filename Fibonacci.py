print("Sequecia de fibo")
n = int(input("Quantos termos Você quer mostrar:"))
t1 = 0
t2 = 1
cont = 3
print("{} > {} ".format(t1,t2), end="")
while cont <= n:
    t3 = t1 + t2
    t2 = t1
    t1 = t3
    print("> {}  ".format(t3), end="")
    cont += 1
print(" Fim")


