# Ejercicio 9 - Mostrar una frase sin espacios y contar

frase = input('Ingrese su frase: ')
frase2 = ""

print(f'Frase inicial: {frase}',end=' ')

for i in frase:
    if i != ' ':
        frase2 += i

frase = frase2
print(f'\nFrase final: {frase}',end=' ')
print(f'\nN° de caracteres: {len(frase)}')