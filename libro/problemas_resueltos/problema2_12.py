SUE = float(input("Sueldo del trabajador:"))
CAT = int(input("Categoria del trabajador:"))
HE = int(input("Horas extras trabajadas:"))

if CAT == 1:
    PHE = 30
if CAT == 2:
    PHE = 38
if CAT == 3:
    PHE = 50
if CAT == 4:
    PHE = 70
if CAT > 4:
    PHE = 0
if HE > 30:
    NSUE = SUE + 30 * PHE
else: 
    NSUE = SUE + HE * PHE 
print(f"El sueldo del trbajador mas las hr extras es { NSUE }")

