# Ejercicio 3 - Pedir numeros hasta encontrar cero, ingresarlos a la lista y luego ordenarlos de menor a mayor

lista = []

numero = int(input('Ingrese un numero: '))

while numero != 0:

    lista.append(numero)

    numero = int(input('Ingrese un numero: '))

lista.sort()

for i in lista:
    print(i,end=' ')