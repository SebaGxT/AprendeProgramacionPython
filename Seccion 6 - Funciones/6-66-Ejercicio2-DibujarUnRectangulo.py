# Ejercicio 2 - Dibujar un rectangulo

def dibujar_rectangulo(alto,ancho):
    for i in range(alto):
        for j in range(ancho):
            print('* ',end='')
        print('\n')

alto = int(input('Ingrese el alto del rectangulo: '))
ancho = int(input('Ingrese el ancho del rectangulo: '))
print('\n')

dibujar_rectangulo(alto,ancho)
    
    

