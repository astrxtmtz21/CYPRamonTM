NOM = 0
SUE = float(int("Cual es el sueldo del trabajador?:"))
while (SUE < > -1):
    if SUE < 1000:
        NSUE = SUE * 1.15
    else:
        NSUE = SUE * 1.12
    NOM = NOM + NSUE
    print(f"El nuevo sueldo del trabajador es { NSUE }")
    OSUE = bool(int(input("Hay mas trabajadores (0 NO / 1 SI)?:")))
print(f"La nomina total de la empresa es { NOM }")

