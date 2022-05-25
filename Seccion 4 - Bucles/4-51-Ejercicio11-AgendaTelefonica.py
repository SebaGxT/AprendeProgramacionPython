# Ejercicio 11 - Agenda Telefonica

Agenda = {}

while True:
    print('\n\t.--Menu Agenda--.')
    print('\n1.Nuevo contacto\n2.Borrar contacto\n3.Ver contactos existentes\n4.Salir\n')
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        print('\n\t.--Crear contacto--.\n')
        while True:
            usuario = input('Ingrese nombre del contacto: ')
            numero = input('Ingrese su numero: ')
            if usuario not in Agenda:
                Agenda[usuario] = {numero}
                print('\nContacto agregado correctamente\n')
            else:
                print('\nUsuario ya existente\n')
            opcion2 = int(input('\nDesea agregar otro contacto 1.Si - 2.No: '))
            print()
            if opcion2 == 2:
                break
    elif opcion == 2:
        print('\n\t.--Eliminar contacto--.\n')
        for clave,valor in Agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
        print()
        while True:
            eliminar = input('\nQue contacto desea eliminar - Ingrese el nombre: ')
            if eliminar in Agenda:
                del(Agenda[eliminar])
                print('\nContacto eliminado correctamente\n')
            else:
                print('\nContacto inexistente\n')
            eliminar2 = int(input('\nDesea continuar eliminando 1.Si - 2.No: '))
            print()
            if eliminar2 == 2:
                break
    elif opcion == 3:
        print('\n\t.--Lista de contactos--.\n')
        for clave,valor in Agenda.items():
            print(f'Nombre: {clave}, Telefono: {valor}')
        print()
    elif opcion == 4:
        print('\n\nCerrando Agenda. Hasta luego')
        break
    else:
        print('\n\nOpcion ingresada incorrecta\n\n')