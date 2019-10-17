PRECIO = float(input("Costo del producto:"))
IMP = 0
if PRECIO > 500:
    IMP = (20 * 0.30) + (PRECIO - 40) * 0.50
elif PRECIO > 40:
    IMP = (20 * 0.30) + (PRECIO - 40) * 0.40
elif PRECIO > 20:
    IMP = (PRECIO - 20) * 0.30
else:
    IMP = 0
PRETOT = PRECIO + IMP
print(f"El precio total del articulo es { PRETOT } con un impuesto de { IMP }")
