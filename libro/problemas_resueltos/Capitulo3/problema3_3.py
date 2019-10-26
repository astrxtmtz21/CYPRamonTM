SERIE = 0
N = int(input("Numero de terminos de la serie:"))
BAND = 'T'
NUM = 1
for i in range (1, N + 1, 1):
    if BAND == 'T':
        SERIE = SERIE + 1 / NUM
        BAND = 'F'
    else:
        SERIE = SERIE - 1 / NUM 
        BAND = 'T'
NUM = NUM + 1
print(f"La serie es { SERIE }")
        
