# Ejercicio 6 - Tabla de Multiplicar

res = []

numero = int(input('Ingrese un valor y se mostrara la tabla de multiplicar del 1 al 10: '))

for i in range(1,11):
    res.append(numero*i)

for i in res:
    print(f'{numero}*{res.index(i)+1}: {i}')