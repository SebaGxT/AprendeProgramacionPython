# Ejercicio 5 - Factorial de un numero Positivo

numero = int(input('Ingrese un numero positivo: '))

while numero <= 0:
    numero = int(input('Ingrese un numero positivo: '))

sum = 1

for i in range(1,numero+1):
    sum *= i

print(f'El resultado factorial de {numero} es: {sum}')