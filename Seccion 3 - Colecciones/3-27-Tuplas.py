# Tuplas - Son otro tipo de coleccion como las listas pero no se pueden modificar una vez creadas - son inmutables - son mas rapidas que las listas consumen menos recursos

nombreTupla = (4,'Hola',6.78,[1,2,3],4,True)

print(nombreTupla)

print(nombreTupla[1])

print(nombreTupla[-1])

print(nombreTupla[1:])

print(4 in nombreTupla)

print(8 not in nombreTupla)

print(nombreTupla.index('Hola'))

print(nombreTupla.count(4))

print(len(nombreTupla))

# Conversion de tupla a lista - la tupla no se modifica se carga la tupla en una  variable nueva creando la lista
lista = list(nombreTupla)

print(lista)

# Conversion de lista a tupla

tupla = tuple(lista)

print(tupla)