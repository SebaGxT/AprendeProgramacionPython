# Errores
"""
    Se divide en dos grandes bloques 
    
    primero los errores cometidos por el programador en la programacion - errores logicos

    segundo los errores cometidos por el usuario - errores funcionales

"""

# Errores sintacticos

#print("Hola Amig@" <- falta de simbolos
#prin("Hola Amig@") <- funcion inexistente
# : falta de : en condicionales, bucles, etc


# Errores semanticos

lista = [1,2,3]

#lista.pop()
#lista.pop()
#lista.pop()
# lista.pop() <- error semantico intenta eliminar mas elementos de los existentes en la lista
# se puede prevenir por ejemplo con un concional antes de mandar a eliminar o bucle que solo recorra esa cantidad

while len(lista)>0:
    print(lista.pop())

print(lista)

# print(lista[5]) <- Acceder a una posicion de una coleccion que no existe


# numero = input('Digite un numero: ') error de tipo de dato al no convertir el input a entero y luego sumar
numero = int(input('Digite un numero: '))
print(f'La suma es: {numero+10}')

# Error de tipo valueError <- digita un numero como cadena ej: "Uno"