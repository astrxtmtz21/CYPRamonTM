numero = int(input("Dame un numero:"))
cantidad= int(input("Dame otra cantidad:"))
cifra = int(input("Una cifra mas:"))

if numero > cantidad and numero > cifra:
   print(f"{Numero} es el mas grande")
if cantidad > cifra and cantidad > numero:
   print(f"{Cantidad} es el mas grande")
if cifra > numero and cifra > cantidad:
    print(f"{cifra} es el mas grande")
print("Fin del programa")
