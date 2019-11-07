def sumar(x, y):
    z = x + y
    return z

def restar (x, y):
    return x - y

def mi_print(texto):
    print(f"Este es mi print: (texto)")

def multiplica( valor, veces ):
    if veces == None :
        print(f"Debes enviar el segundo argumento de la funcion")
    else:
        print(valor * veces)

def comanda(mesa, comensal, entrada, medio, fuerte, postre):
    print(f"Mesa: {mesa} comensal: {comensal}")
    print(f"\t Entrada: {entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte: { fuerte }")
    print(f"\t Postre: { postre }")

def imprime_argumentos( *argumentos):
    print('---->',argumentos, '<----')

a = 10
b = 5
c = sumar(a,b)
print(f"La suma de {a} y {b} es {c }")
c = restar (a,b)
print(f"La resta de {a} y {b} es {c}")
mi_print("Hola!!!")
imprime_argumentos('Hola', True, 3.1416, ('id' : 'ac01', 'nombre' : 'Juan')

