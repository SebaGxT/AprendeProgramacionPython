# Ejercicio 1 - Cambio de divisas

def cambio_divisa(moneda,ope):
    
    tipocambio = 200

    if ope == 1:
        return moneda/tipocambio
    else:
        return moneda*tipocambio
 
while True:
    print("""
    
...Menu principal...

1. Compra Dólares
2. Venta Dólares
3. Salir

    """)

    opcion = int(input('Ingrese la opcion a realizar: '))

    if opcion == 1:
        while True:
            moneda = float(input('Ingrese el monto de dinero: '))
            if moneda > 0:
                break
            else:
                print('\n\nMonto invalido. Debe ingresar un monto positivo') 
        print(f'El cambio de divisas: U$D {cambio_divisa(moneda,1):.2f}')
    elif opcion == 2:
        while True:
            moneda = float(input('Ingrese el monto de dinero: '))
            if moneda > 0:
                break
            else:
                print('\n\nMonto invalido. Debe ingresar un monto positivo')
        print(f'El cambio de divisas: $ {cambio_divisa(moneda,2):.2f}')
    elif opcion == 3:
        print('\n\nHasta luego\n\n')
        break
    else:
        print('\n\nOpcion incorrecta')