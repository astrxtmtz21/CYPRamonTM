MAT = int(input("Matricula del alumno:"))
CAR = str(input("Carrera en la que esta inscrito:"))
SEM = int(input("Semestre:"))
PRO = float(input("Promedio del alumno:"))

if CAR == "Economia":
    if SEM >= 6 and PRO >= 8.8:
        print(f"El alumno con matricula { MAT } y carrera { CAR } es aceptado!")
elif CAR == "Computacion":
    if SEM > 6 and PRO > 8.5:
        print(f"El alumno con matricula { MAT } y carrera { CAR } es aceptado!")
elif CAR == "Administracion":
    if SEM > 5 and PRO > 8.5:
        print(f"El alumno con matricula { MAT } y carrera { CAR } es aceptado!")
elif CAR == "Economia":
    if SEM > 5 and PRO > 8.5:
        print(f"El alumno con matricula { MAT } y carrera { CAR } es aceptado!")

