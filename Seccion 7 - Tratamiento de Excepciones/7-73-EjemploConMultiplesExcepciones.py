# Multiples excepciones

def dividir():
    while True:
        try:
            n1 = float(input('Ingrese un numero: '))
            n2 = float(input('Ingrese otro numero: '))

            res = n1/n2
            print(f'El resultado de la division es: {res:.2f}')
        except ValueError:
            print('Error -> Digite correctamente los valores numericos')
        except ZeroDivisionError:
            print('No se puede realizar una division entre 0')
        else:
            break
    
dividir()