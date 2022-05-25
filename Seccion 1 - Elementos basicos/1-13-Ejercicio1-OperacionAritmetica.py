from contextlib import AbstractAsyncContextManager
from re import A


# Ejercicio 1

a = float(input("Ingrese un valor: "))
b = float(input("Ingrese un valor: "))
c = float(input("Ingrese un valor: "))

res = (a**3 * (b**2 - 2*a*c)) / (2*b)

print(f'El resultado de la operacion es: {res}')

