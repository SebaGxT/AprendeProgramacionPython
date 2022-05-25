# Ejercicio 1 numeros pares e impares

n = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese un segundo numero: '))

if n % 2 == 0 and n2 % 2 == 0:
    print('Ambos numeros son pares')
elif not(n % 2 == 0 and n2 % 2 == 0):
    print('Ambos numeros son impares')
else:
    if n % 2 == 0:
        print('El primer numero ingresado es par')
    else:
        print('El primer numero ingresado es impar')
    if n2 % 2 == 0:
        print('El segundo numero ingresado es par')
    else:
        print('El segundo numero ingresado es impar')
