# Listas - son estructuras de datos mas flexibles - funcionan como arreglos o vectores

lista = ['Lunes','Martes','Miercoles','Jueves','Viernes',40,5.67,[1,2,3],True] # Admite cadenas, enteros, flotantes, booleanos, otras listas

print(lista) # imprime todos los elementos de la lista

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

print(lista[-1]) # con el numero negativo accede a la lista desde el final al principio

# Sublista

print(lista[0:3]) # llega hasta una posicion antes del limite maximo

print(lista[:3]) # si no se especifica el inicio, python interpreta que empieza al inicio

print(lista[1:4])

print(lista[2:]) # imprime desde la posicion indicada hasta el final

print(len(lista)) # funcion para cantidad de elementos de lista

lista2 = [1,2,4,5]

# Ingresar elementos en lista

lista2.append(6) # agrega elementos al final de la lista
lista2.append('Sebastian')

# Agregar elementos en posicion especifica
# (posicion,elemento)
lista2.insert(2,3)

print(lista2)

# Agregar varios elementos al final de la lista

lista2.extend([7,8,9])

print(lista2)

# concatenar listas

lista3 = lista+lista2

print(lista3)

# buscar elementos dentro de la lista

print(3 in lista2)

print(9 not in lista2)

# conocer indice del elemento buscado en lista

print(lista2.index('Sebastian'))

# conocer cantidad de valores repetidos
lista4 = [1,1,1,1]

print(lista4.count(1))

# eliminar elementos de la lista

lista3.pop() # si no se pasa un paramentro elimina el ultimo elemento
print(lista3)

lista3.pop(2) # se especifica indice para eleminar el elemento en esa posicion

# especificar elemento que queres eliminar sin saber posicion

lista3.remove(True)
print(lista3)

# eliminar toda la lista
lista3.clear()
print(lista3)

# voltear la lista
lista.reverse()
print(lista)

# copiar los elementos de la lista
lista5 = [1,4,5,6,'Male']*2
print(lista5)

# ordena elementos de la lista
lista6 = [5,4,-7,9,0,1,3]
lista6.sort() # ordena de menor a mayor
print(lista6)
lista6.sort(reverse=True) # ordena de mayor a menor
print(lista6)