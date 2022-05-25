# Ejercicio 2 - mayor de 3 numeros
n = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

if n >= n2 and n >= n3:
    print(f'El numero mayor es {n}')
elif n2 >= n and n2 >= n3:
    print(f'El numero mayor es {n2}')
elif n3 >= n and n3 >= n2:
    print(f'El numero mayor es {n3}')
