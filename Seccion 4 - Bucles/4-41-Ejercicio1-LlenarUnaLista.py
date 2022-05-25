# Ejercicio 1 - Llenar una lista

'''
Creacion de una lista numerica con valores ordenados en una linea - solo se puede con valores numericos

lista = list(range(1,51))

'''

lista = []

for i in range(1,51):
    lista.append(i)

for i in lista:
    if i == len(lista):
        print(f'{i}',end=' ')
    else:
        print(f'{i} - ',end=' ')