MAY = -100000
MEN = 100000
N = int(input("Numero de datos a ingresar:"))
for i in range (1, N+1, 1):
    NUM = int(input("Ingrese un numero entero:"))
    if NUM > MAY:
        MAY = NUM
    if NUM < MEN:
        MEN = NUM 
    N = N + 1
print(f"El numero mayor de todos es { MAY } y el menor { MEN }")
