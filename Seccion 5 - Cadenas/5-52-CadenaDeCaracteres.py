# Cadena de Caracteres

from lib2to3.pgen2.literals import simple_escapes


simples = 'Hola mundo simple'
dobles = "Hola mundo dobles"
mixto = 'Estoy "Estudiando" '
mixto2 = "Estoy 'Estudiando 2' "
simplesSimples = 'Estoy \'Estudiando 3\' '
doblesDobles = "Estoy \"Estudiando 4\" "
tabulacion = "\tEstoy Estudiando 5"
saltoLinea = "Estoy \nEstudiando 6"
msjCrudo = r"D:\nombre\trabajos" # Mensaje se guarda sin procesar - evita la confusion de la ruta con los saltos de linea u otros comandos como tabulacion por la barra invertida
textoVariasLineas = """ Hola
Como estas?
Mi nombre es Sebastian
"""
cadena1 = "Hola "
cadena2 = "Que tal?"

print(simples)
print(dobles)
print(mixto)
print(mixto2)
print(simplesSimples)
print(doblesDobles)
print(tabulacion)
print(saltoLinea)
print(msjCrudo)
print(textoVariasLineas)
print("""  Texto varias 
Lineas en el 
print
"""
)
print(cadena1+cadena2)