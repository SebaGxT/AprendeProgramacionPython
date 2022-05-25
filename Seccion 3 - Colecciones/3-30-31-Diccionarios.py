# Diccionarios - contienen dos elementos por posicion {Clave:valor,} no puede tener claves duplicadas pero si valores

diccionario = {} # Declaracion de diccionario vacio

print(diccionario)

dic = {"azul":"blue","rojo":"red","verde":"green"} # Admite el ingreso de enteros, reales, caracteres, otras colecciones listas tuplas conjuntos y otros diccionarios

# para imprimir un valor se ingresa su clave entre corchetes
print(dic["azul"])
print(dic["rojo"])
print(dic["verde"])

# Agregar elementos
dic["amarillo"] = "yellow"
print(dic)

# Modificar
dic["azul"] = "BLUE"
print(dic)

# Eliminar - al eleminar la clave elimina tambien el valor
del(dic["verde"])
print(dic)

# agregar otra coleccion
dic = {"Sebastian":{"Edad":27,"Altura":1.67},"Marlene":[22,1.66]}

print(dic)

equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario Mandzukic"}

# En diccionario es clave no indice
print(equipo[10])

# Clave inexistente muestra una excepcion
#print(equipo[6])

# Mostrar mensaje para claves inexistentes
print(equipo.get(6,"No existe dentro del diccionario esa clave"))

# busqueda en diccionario
print(10 in equipo)
print(6 not in equipo)

# Imprimir claves
print(equipo.keys())

# Imprimir valores
print(equipo.values())

# Imprimir clave valor - se suele utilizar para recorrer diccionarios con bucles for
print(equipo.items())

# Contar elementos
print(len(equipo))

# Eliminar todos los elementos
equipo.clear()
print(equipo)
