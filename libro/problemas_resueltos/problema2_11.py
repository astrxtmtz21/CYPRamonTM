CLAVE = int(input("Clave de la zona geografica:"))
NUM = int(input("Duracion en minutos de la llamada:"))

if CLAVE == 12:
    COST = NUM * 2
if CLAVE == 15:
    COST = NUM * 2.2
if CLAVE == 18:
    COST = NUM * 4.5
if CLAVE == 19:
    COST = NUM * 3.5
if CLAVE == 23:
    COST = NUM * 6
if CLAVE == 25:
    COST = NUM * 6
if CLAVE == 29:
    COST = NUM * 5
print(f"El costo de la llamada es de { COST }")
