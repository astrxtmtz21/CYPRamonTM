MED = 0
CHI = 0
GRA = 0
N = int(input("Numero de ventas del vendedor:"))
for i in range (1, N+1, 1):
    V = float(input("Cantidad de la venta realizada:"))
    if V <= 200:
        CHI = CHI + 1
    if V < 400:
        MED = MED + 1
    else:
        GRA = GRA + 1
N = N + 1
print(f"La ventas iguales o menores a 200 fueron { CHI }, las mayores a 200 y menores a 400 fueron { MED } y las mayores a 400 fueron { GRA }")
