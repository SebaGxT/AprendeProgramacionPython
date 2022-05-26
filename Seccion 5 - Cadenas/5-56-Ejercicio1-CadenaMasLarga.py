# Ejercicio 1 - La cadena mas larga

cadena1 = input('Ingrese la primer palabra: ')
cadena2 = input('Ingrese la segunda palabra: ')

if len(cadena1) == len(cadena2):
    print(f'Ambas cadenas tienen la misma cantidad de caracteres: {len(cadena1)}')
elif len(cadena1) > len(cadena2):
    print(f'La primer palabra {cadena1} tiene {len(cadena1)} caracteres y es la mas larga')
else:
    print(f'La segunda palabra {cadena2} tiene {len(cadena2)} caracteres y es la mas larga')