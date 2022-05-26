# Cadenas de caracteres - Metodos para cadenas

# mayusculas
cadena = 'hola mundo'.upper()
print(cadena)

# minusculas
cadena = 'HOLA MUNDO'.lower()
print(cadena)

# Primera letra mayuscula
cadena = 'hola mundo'.capitalize()
print(cadena)

# Primera letra en cada palabra mayuscula
cadena = 'hola mundo'.title()
print(cadena)

# Contar letras
cadena = 'hola mundo'.count('o')
print(cadena)

# Contar palabras
cadena = 'hola mundo'.count('mundo')
print(cadena)

# Busca y muestra el indice de primer coincidencia
cadena = 'hola mundo mundo mundo'.find('mundo')
print(cadena)

# Busca y muesta el indice de la ultima coincidencia
cadena = 'hola mundo mundo mundo'.rfind('mundo')
print(cadena)

# consulta de cadenas si son todos numeros
cadena = '1000'.isdigit()
print(cadena)

cadena = '1000a'.isdigit()
print(cadena)

# Consulta de cadenas si son todos alfabeticos
cadena = 'Asqt'.isalpha()
print(cadena)

cadena = 'Asqt?'.isalpha()
print(cadena)

# Consulta de cadenas alfanumericos
cadena = 'Asqt1'.isalnum()
print(cadena)

cadena = 'Asqt1='.isalnum()
print(cadena)

# Consulta de cadenas si solo tiene minusculas
cadena = 'hola mundo'.islower()
print(cadena)

cadena = 'hola mundO'.islower()
print(cadena)

# Consulta de cadenas si solo tiene mayusculas
cadena = 'HOLA MUNDO'.isupper()
print(cadena)

cadena = 'HOLA MUNDo'.isupper()
print(cadena)

# Consulta de cadenas si es titulo con cada primer letra mayuscula
cadena = 'Hola Mundo'.istitle()
print(cadena)

cadena = 'Hola mundo'.istitle()
print(cadena)

# Consulta si la cadena es de solo espacios en blanco
cadena = '     '.isspace()
print(cadena)

cadena = '       x'.isspace()
print(cadena)

# startswith - retorna booleano - indica si la cadena comienza con el parametro de coindicencia que se pasa a la funciona
cadena = 'hola mundo'.startswith('h')
print(cadena)

cadena = 'hola mundo'.startswith('x')
print(cadena)

# endswith - retorna booleano - indica si la cadena finaliza con el parametro de coincidencia que se pasa a la funcion
cadena = 'hola mundo'.endswith('mundo')
print(cadena)

cadena = 'hola mundo'.endswith('x')
print(cadena)

# metodo split - divide los elementos de la cadena por los espacios en blanco y los coloca en una lista
cadena = 'hola mundo'.split()
print(cadena)

# split separa los elementos indicando un parametro
cadena = 'hola-mundo'.split('-')
print(cadena)

# Join - separa los elementos de la cadena indicando con que elemento los separa
cadena = ','.join('Sebastian')
print(cadena)

# Elimina espacios en blanco que no sirven
cadena = '    hola     '.strip()
print(cadena)

# Elimina elementos pasados por parametro
cadena = '.......Hola.......'.strip('.')
print(cadena)

# Metodo replace - reemplaza caracteres o palabras - 'asdaf'.replace('palabra a reemplazar','reemplazo')
cadena = 'hola mundo'.replace('o','0')
print(cadena)

cadena = 'hola mundo'.replace('hola','HOLA')
print(cadena)
