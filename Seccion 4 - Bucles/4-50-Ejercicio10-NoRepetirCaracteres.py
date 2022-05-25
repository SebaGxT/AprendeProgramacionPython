# Ejercicio 10 - No Repetir caracteres

cadena = input('Ingresar una cadena: ')

lista = []

for i in cadena:
    if i not in lista:
        lista.append(i)

print(lista)