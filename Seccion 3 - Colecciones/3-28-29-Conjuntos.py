# Conjuntos - son grupos de elementos desordenados donde no pueden existir elementos duplicados
# Se debe indicar primero el set ya que si no python crea un diccionario y no un conjunto ya que diccionario y conjuntos se crean con {}
conjunto = set()

conjunto = {1,2,3,'Hola',4.56} # no admite otro tipo de coleccion dentro de los conjuntos - por ejemplo no admite listas

print(conjunto)

# Agregar elementos al conjunto - agrega el elemento en la posicion que quiere el conjunto
conjunto.add(5)
conjunto.add('Adios')
conjunto.add('a')
print(conjunto)

# Eliminar elemento del conjunto
conjunto.discard(3)
conjunto.discard('Hola')
print(conjunto)

# Buscar elementos
print(1 in conjunto)

# Buscar si no hay un elemento
print(3 not in conjunto)

# Vaciar conjunto
conjunto.clear()
print(conjunto)

# creacion de conjuntos inicializados con elementos separados por coma se crea correctamente ya que los diccionarios usan dos puntos : , por lo tanto no es necesario crear el set solamente se usan cuando se agregan elementos posteriormente con add

a = {1,2,3}
b = {3,4,5}

# comparar dos conjuntos - no importa el orden si tienen los mismo elementos son iguales
print ( a == b)

# Operaciones que se pueden realizar con los conjuntos

# Union

c = a | b

print(c)

# Interseccion

c = a & b

print(c)

# Diferencia del conjunto a

c = a - b

print(c)

# Diferencia del conjunto b

c = b - a

print(c)

# Diferencia simetrica 

c = a ^ b

print(c)

# Determinar subconjuntos

d = {1,2,3,4,5}

print(a.issubset(d))
print(b.issubset(d))

# Determinar Superconjunto
print(d.issuperset(a))

# Disconexos -verifica si comparten elementos o no
print(a.isdisjoint(b))

# Conjuntos inmutables - no se pueden modificar
e = frozenset({1,2,7})

print(e)

