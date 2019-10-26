BAND = 'T'
SUMSER = 0
VALOR = 2
for i in range (2, 1801, 1):
    SUMSER = SUMSER + 1
    print(f"El siguiente numero es { VALOR }")
    if BAND == 'T':
        BAND == 'F'
        VALOR = VALOR + 3
    else:
        BAND == 'T'
        VALOR = VALOR + 2
print(f"La suma de la serie es { SUMSER }")
