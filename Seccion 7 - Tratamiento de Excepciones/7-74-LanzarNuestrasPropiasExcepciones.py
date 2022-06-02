# Lanzar excepciones Propias

def verificandoEdad(edad):
    if edad<0:
        raise ValueError ('La edad no puede ser negativa')
    elif edad<18:
        print('Eres muy joven')
    elif edad<30:
        print('Eres joven')
    elif edad<50:
        print('Eres maduro')

edad = int(input('Ingrese su edad: '))
try:
    verificandoEdad(edad)
except ValueError as EdadNegativa: #as da nombre propio al tipo de error capturado
    print(EdadNegativa) # Muestra el mensaje programado en el raise
print('Programa terminado')