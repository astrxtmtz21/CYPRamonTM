CATE = int(input("Cual es la categoria del trabajador?:"))
SUE = float(input("Cual es su sueldo?:"))
NSUE = 0
if CATE == 1:
    NSUE = SUE * 1.15
elif CATE == 2:
    NSUE = SUE * 1.10
elif CATE == 3:
    NSUE = SUE * 1.08
elif CATE == 4:
    NSUE = SUE * 1.07

print(f"Dada la categoria { CATE } el nuevo sueldo del trabajador es { NSUE }")
