# Ejercicio 7 - Juego Adivina el Numero - Se debe generar un numero aleatorio entre 0 - 100 y luego pedir numero indicando si es mayor o menor respecto a N. 
# El proceso termina cuando el jugador acierta el numero

import random

n = random.randint(0,100)

numero = int(input('Ingrese un numero para adivinar: '))

contador = 0

while numero != n:

    if numero < n:
        print('No es el numero ingrese uno mas grande')
        numero = int(input('Ingrese un numero: '))
        contador += 1
    else:
        print('No es el numero ingrese uno mas chico')
        numero = int(input('Ingrese un numero: '))
        contador += 1

print(f'\n\nAdivino el numero: {n}')
print(f'\n\nCantidad de intentos: {contador}')