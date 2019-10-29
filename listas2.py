# arreglos
# lectura
# escritura / asignacion
# actualizacion
# ordenamiento
# busqueda

# Escritura
frutas = ["Zapote", "Manzana", "Pera", "Aguacate", " Durazno", "Uva", "Sandia"]

# Lectura
print(frutas[2])

#Lectura con for
# For opcion 1

for indice in range(0, 7, 1):
    print(frutas[indice])
print("-----")

#For opcion2 - por un iterador for each

for fr in frutas:
    print(fr)

#Asignacion
frutas[2]="Melon"
print(frutas)

#Insercion al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2, "Limon")
print(frutas)
print(len(frutas))
frutas.insert(0,"Mamey")
print(frutas)

#Eliminacion con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas[2]="Limon"
frutas.append("Limon")
print(frutas)
frutas.remove("Limon")
print(frutas)

#Ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#Busqueda
print(f"La Uva esta en la pos. { frutas.index('Uva') } ")
print(f"El limon esta { frutas.count('Limon') } veces en la lista")

#Concatenar
print(frutas)
otras_frutas = ["Rambutan", "Platano", "Fresa", "Toronja"]
frutas.append(otras_frutas)
print(frutas)

#Copiar
copia = frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia = frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(otra_copia)
