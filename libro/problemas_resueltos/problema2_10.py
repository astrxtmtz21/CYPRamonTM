A = int(input("Dame un numero(A):"))
B = int(input("Dame un segundo numero(B):"))
C = int(input("Dame un tercer numero(C):"))

if A > B:
    if A > C:
        print:(f" { A } es el mayor")
    elif A == C:
        print(f"{ A } Y { C } son los mayores")
    else:
        print(f"{ C } es el mayor")
elif A == B:
    if A > C:
        print(f"{ A } y { B } son mayores")
    elif A == C:
        print(f"{ A }, { B } y { C } son iguales")
    else:
        print(f"{ C } es el mayor")
elif B > C:
        print(f"{ B } es el mayor")
elif B == C:
        print(f"{ B } y { C } son los mayores")
else:
    print(f"{ C } es el mayor")



