SERIE = 0
N = int(input("Numero de terminos de la serie:"))
for i in range (1, N+1, 1):
    SERIE = SERIE + N ** N
    N = N + 1
print(f"La suma de la serie es { SERIE }")
