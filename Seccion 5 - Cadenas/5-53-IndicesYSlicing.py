# Cadenas de Caracteres - Indices y Slicing

cadena = "Sebastian"

# Toda la cadena
print(cadena)

# Un caracter - Funciona como las colecciones - las cadenas tienen indices
print(cadena[0])
print(cadena[1])
print(cadena[2])
print(cadena[3])
print(cadena[-1])
print(cadena[-2])

# Slicing
print(cadena[1:4])
print(cadena[:5])
print(cadena[3:])

# Las cadenas son inmutables - no permite modificar directamente - ej: cadena[0] = 'a' - muestra mensaje de error
# Para modificarlas se puede hacer lo siguiente
cadena = 's' + cadena[1:]
print(cadena)
