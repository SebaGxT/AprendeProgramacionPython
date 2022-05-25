# Ejercicio 5 - Cajero Automatico

saldoInicial = 1000.00

print('\n\n1. Ingresar dinero en la cuenta\n2. Retirar dinero de la cuenta\n3. Mostrar dinero disponible\n4. Salir\n\n')

opcion = int(input('Ingrese la operacion que desea realizar: '))

if opcion == 1:
    print(f'Saldo actual: ${saldoInicial:.2f}')
    saldo = float(input('Ingrese monto a depositar: '))
    if saldo <=0:
        print('Monto ingresado invalido')
    else:
        saldoInicial += saldo
        print('\n\nProcesando...\n\n')
        print(f'Saldo actual: ${saldoInicial:.2f}')
elif opcion == 2:
    if saldoInicial == 0:
        print(f'No es posible realizar extraccion.\nSaldo actual: ${saldoInicial:.2f}')
    else:
        print(f'Saldo actual: ${saldoInicial:.2f}')
        saldo = float(input('Ingrese monto a extraer: '))
        if saldo <= 0:
            print('Monto ingresado invalido')
        else:    
            if saldo > saldoInicial:
                print('No es posible retirar. Saldo insuficiente ')
            else:
                saldoInicial -= saldo
                print('\n\nRetire el dinero...\n\n')
                print(f'Saldo actual: ${saldoInicial:.2f}')
elif opcion == 3:
    print(f'Saldo actual: ${saldoInicial:.2f}')
elif opcion == 4:
    print('Cerrando Sesion...Hasta luego')
else:
    print('Opcion incorrecta')

