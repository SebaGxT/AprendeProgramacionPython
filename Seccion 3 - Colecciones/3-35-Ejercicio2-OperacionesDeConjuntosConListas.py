'''
Ejercicio 2 - Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

Lista de palabras que aparecen en las dos listas
lista de palabras que aparecen en la primera lista, pero no en la segunda
lista de palabras que aparecen en la segunda lista, pero no en la primera
lista de palabras que aparecen en ambas listas


'''

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

a = set(lista1)
b = set(lista2)

c = list(a | b)
print(c)

c = list(a - b)
print(c)

c = list(b - a)
print(c)

c = list(a & b)
print(c)
