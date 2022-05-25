# Ejercicio 4 - Sumar Pares dentro de un rango

mini = int(input('Ingrese un valor minimo: '))
maxi = int(input('Ingrese un valor maximo: '))
sum = 0

for i in range(mini,maxi+1):
    if i %2 == 0:
        sum += i

print(sum)