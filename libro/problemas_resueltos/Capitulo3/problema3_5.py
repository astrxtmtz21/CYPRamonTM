SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Numero de datos:"))
for i in range (1, N+1, 1):
    NUM = int(input("Dame un numero entero:"))
    if NUM > 0:
        SUMPOS = SUMPOS + NUM
        CUEPOS = CUEPOS + 1
    else:
        SUMOTR = SUMOTR = SUMOTR + 1
    N = N + 1
PROGEN = (SUMPOS + SUMOTR) / N
PROPOS = (SUMPOS / CUEPOS)
print(f"El promedio de todos los numeros es { PROGEN }, los mayores a cero son { CUEPOS } y el promedio de los numeros positivos es { PROPOS }")
