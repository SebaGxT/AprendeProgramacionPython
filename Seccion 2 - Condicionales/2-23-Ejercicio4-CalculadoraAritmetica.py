# Ejercicio 4 - Calculadora Aritmetica

print('Para realizar una operacion debe indicar con la primer letra que operacion quiere realizar\nS -> Suma - R -> Resta - M -> Multiplicacion - D -> Division\n\n ')

ope = input('Ingrese la letra de la operacion: ').lower()

if ope == 's' or ope == 'r' or ope == 'm' or ope == 'd':

    n = float(input('Ingrese el primer numero: '))
    n2 = float(input('Ingrese el segundo numero: '))

    if ope == 's':
        res = n + n2
        print(f'El resultado es: {res:.2f}')
    elif ope == 'r':
        res = n - n2
        print(f'El resultado es: {res:.2f}')
    elif ope == 'm':
        res = n * n2
        print(f'El resultado es: {res:.2f}')
    elif ope == 'd':
        if n2 == 0:
            print('No se puede dividir por cero')
        else:
            res = n / n2
            print(f'El resultado es: {res:.2f}')
else:
    print('Valor ingresado incorrecto')
