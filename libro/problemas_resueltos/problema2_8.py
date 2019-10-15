C = float(input("Monto de la compra:"))

if C < 500:
    P = C
elif C <= 1000:
    P = C - (C * 0.05)
elif C <= 7000:
    P = C - (C * 0.11)
elif C <= 15000:
    P = C - (C * 0.18)
else:
    P = C - (C * 0.25)
print(f"El total a pagar es { P }")

