# arreglos
# lectura
# escritura / asignacion
# actualizacion
# ordenamiento
# busqueda

# Escritura
frutas = ["Manzana", "Pera", "Aguacate", " Durazno", "Uva", "Sandia"]

# Lectura
print(frutas[2])

#Lectura con for
# For opcion 1
for indice in range(0,7,1):
    print(frutas[indice])

#For opcion2 - por un iterador for each

for fr in frutas:
    print(fr)

#Asignacion
frutas[2]="Melon"
print(frutas)
