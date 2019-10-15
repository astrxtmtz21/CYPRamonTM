MAT = int(input("Numero de matricula:"))
CAL1 = float(input("Primera calificacion:"))
CAL2 = float(input("Segunda calificacion:"))
CAL3 = float(input("Tercera calificacion:"))
CAL4 = float(input("Cuarta calificacion:"))
CAL5 = float(input("Quinta calificacion:"))

PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5) / 5

if PRO >= 6:
    print(f"Tu promedio es { PRO } y estas aprobado!")
else:
    print(f"Tu promedio es { PRO } y estas reprobado")
