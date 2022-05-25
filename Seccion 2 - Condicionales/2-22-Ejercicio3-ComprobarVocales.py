# Ejercicio 3 - Comprobar Vocales

letra = input('Ingrese una letra: ').lower()

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'{letra} es una vocal')
else:
    print(f'{letra} no es una vocal')