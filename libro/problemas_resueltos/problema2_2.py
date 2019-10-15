P = int(input("Valor de P:"))
Q = int(input("Valor de Q:"))

EXP = P ** 3 + Q ** 4 - 2 * P ** 2
if EXP < 680:
    print(f"Calculo auxiliar es { EXP } y como resultado { P } y { Q }")
