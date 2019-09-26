SUE = float(input("Cual es el sueldo?:"))

if SUE < 1000:
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print(f"El nuevo sueldo es { NSUE }")
if SUE > 1000:
    print(f"El sueldo es el mismo { SUE }")
