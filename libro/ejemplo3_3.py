CUECER = 0
N = int(input("Numero de datos:"))
for i in range(0, N, 1):
    NUM = int(input("Numero entero:"))
    if NUM == 0:
        CUECER += 1 
print("El numero de 0's capturados fue:",CUECER)

