n = s = c = 0
while True:
    n = int(input("Digite um valor [999 Se quiser parar]"))
    if n == 999:
        break
    s += n
    c += 1
print(f"A Soma total foi {s} e foram digitados {c} numeros")
