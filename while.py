otra =  bool(int(input("Hay mas alumnos (0 NO, 1 SI):")))
suma = 0.0
cont = 0
while(otra == True):
    cal = float(input("Calificacion:"))
    cont += 1
    suma += cal
    otra = bool(int(input("Hay mas alumnos (0 NO, 1 SI):")))
print("Suma",suma)
print("Promedio:",suma/cont)

