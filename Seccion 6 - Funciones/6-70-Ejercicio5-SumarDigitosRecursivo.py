# Ejercicio 5 - Sumar digitos con recursividad

def sumar_digitos(num):
    if num == 0:
        resultado = 0
    else:
        resultado = sumar_digitos(int(num/10))+(num%10)
    return resultado


print(f'{sumar_digitos(123)}')
print(f'{sumar_digitos(5498)}')