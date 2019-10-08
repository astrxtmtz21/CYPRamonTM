A = int(input("Numero entero positivo:"))
B = int(input("Segundo numero entero positivo:"))
C = int(input("Tercer numero entero positivo:"))

if A > B :
    if A > C:
        if B > C:
            print(f"{ A }, { B }, { C }")
        else:
            print(f" { A }, { C }, { B }")
    else:
        print(f"{ C }, { A }, { B }")
else:
    if B > C:
        if A > C:
            print(f"{ B }, { A } y { C }")
        else:
            print(f"{ B }, { C } y { A }")
    else:
        print(f"{ C }, { B }, y { A }")
