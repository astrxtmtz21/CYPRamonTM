NUM = int(input("Ingrese cualquier numero positivo:"))
if NUM > 0:
    if NUM != 1:
        print(f"El numero es { NUM }")
        if (-1 ** NUM) > 0:
            NUM = NUM / 2
        else:
            NUM = NUM * 3 + 1
    print(f"El numero es { NUM }")
else:
    print(f"Tiene que ingresar un numero entero positivo")
