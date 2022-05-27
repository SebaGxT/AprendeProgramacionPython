# Ejercicio 5 - Contar vocales en una cadena

cadena = input('Ingrese una cadena: ')

print(
    f"""
    Cantidad de vocales en la cadena

    Vocal a: {cadena.count('a')}
    Vocal e: {cadena.count('e')}
    Vocal i: {cadena.count('i')}
    vocal o: {cadena.count('o')}
    vocal u: {cadena.count('u')}
    Total: {cadena.count('a')+cadena.count('e')+cadena.count('i')+cadena.count('o')+cadena.count('u')}
    """
)