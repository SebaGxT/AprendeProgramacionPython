# Ejercicio 4 - Factorial Recursivo

def factorial(n):
    if n > 0:
        resultado = n * factorial(n-1)
    else:
        resultado = 1
    return  resultado

res = factorial(5)
print(res)
