# Ejercicio 3 - Palabra O Frase Palindroma

cadena = input('Ingrese una cadena: ')

# Reemplaza espacio en blanco por nada
cadena = cadena.replace(" ","")

# copia la cadena invertida en otra variable
cadena2 = cadena[::-1]

if cadena == cadena2:
    print(f'La cadena {cadena} es palindroma')
else:
    print(f'La cadena {cadena} no es palindroma')
