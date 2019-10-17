TENF = int(input("Tipo de enfermedad:"))
EDAD = int(input("Edad del paciente:"))
DS = int(input("Numero de dias hospitalizado:"))

if TENF == 1:
    COST = DS * 25
elif TENF == 2: 
    COST = DS * 16
elif TENF == 3:
    COST = DS * 20
elif TENF == 4:
    COST = DS * 32
if EDAD >= 14 and EDAD <= 22:
    COST = COST * 1.10 

print(f"El costo total que representa el paciente es { COST }")

