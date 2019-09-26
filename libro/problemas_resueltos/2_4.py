SUE = float(input("Cual es el sueldo?:"))

if SUE < 1000:
    NSUE = SUE * 1.15
    print(f"El sueldo es { NSUE }")
if SUE > 1000:
    NSUE = SUE * 1.12
    print(f"El sueldo es { NSUE }")
