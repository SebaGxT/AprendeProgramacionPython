# Bucle For
# En python el bucle for se utiliza con colecciones, tiene un iterador que recorre los elementos de una coleccion - puede ser una lista, tupla, conjunto, diccionario, cadena
# Toma la cantidad de elementos de la colleccion para la cantidad de iteraciones del for

coleccion = [2,10,3,4,"Sebastian"]

for i in coleccion:
    print(f'El elemento de la coleccion es: {i}')

diccionario = {"Sebastian":27,"Marlene":22,"Luna":0.3}

for i in diccionario:

    # Solo Clave
    print(f'La Clave de la coleccion es: {i}')

    # Solo valor
    print(f'El valor de la coleccion es: {diccionario[i]}')

    # Clave valor
    print(f'{i} -> {diccionario[i]}')

for clave,valor in diccionario.items():
    print(f'{clave} -> {valor}')

cadena = "Sebastian"

for i in cadena:

    # Impresion de caracter a caracter con salto de linea
    print(f'{i}')

for i in cadena:
    
    print(f'{i}',end=' ')
