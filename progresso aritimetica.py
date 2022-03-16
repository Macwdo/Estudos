s = 0
pt = int(input("Digite o primeiro termo da pa:"))
r = int(input("Digite a razão da pa:"))
for c in range(0, 10):
    rz = r * c
    x = pt + rz
    print("{}".format(x), end="-")
print("fim")