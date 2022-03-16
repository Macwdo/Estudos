pt = int(input("Digite o primeiro termo da P.A:"))
rz = int(input("Digite a razão da P.A:"))
x = 0
print("{}".format(pt), end=">")
while x != 9:
    x += 1
    rt = rz * x
    pa = pt + rt
    print("{}".format(pa),end=">")
print("\nFim Da Pa")