# Ejercicio 3 - Menu Para Clientes

def agregar_cliente(clientes):
    print('\n\t..---Agregar cliente---..\n')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    while True:
        dni = input('Ingrese el dni: ')
        if not dni.isdigit():
            print('\n\t..---Debe ingresar numeros sin puntos---..\n')
        else:
            if not dni in clientes:
                clientes[dni] = {"nombre":nombre,"apellido":apellido}
                print('\n\t..---Cliente Agregado Correctamente---..\n')
                break
            else:
                print('\n\t..---Cliente ya existente en la agenda---..\n')
                nombre = input('Ingrese el nombre: ')
                apellido = input('Ingrese el apellido: ')
def mostrar_clientes(clientes):
    print('\n\t..---Resultados---..')
    if len(clientes) > 0:
            for i in clientes:
                print(f'DNI: {i}\nNombre: {clientes[i]["nombre"]}\nApellido: {clientes[i]["apellido"]}\n')
    else:
        print('\n\t..---Resultado---..')
        print('\nLista de clientes vacia')
def mostrar_cliente_dni(clientes):
    print('\n\t..---Mostrar Cliente por DNI---..\n')
    if len(clientes) > 0:
        while True:
            dni = input('Ingrese el dni: ')
            if not dni.isdigit():
                print('\n\t..---Debe ingresar numeros sin puntos---..\n')
            else:
                break
        cliente = clientes.get(dni,"Dni inexistente")
        if cliente != 'Dni inexistente':
            print('\n\t..---Resultado---..')
            print(f'\nDNI: {dni}\nNombre: {cliente["nombre"]}\nApellido: {cliente["apellido"]}\n')
        else:
            print('\n\t..---Resultado---..')
            print('Dni inexistente\n')
    else:
        print('\n\t..---Resultado---..')
        print('\nLista de clientes vacia')
def eliminar_cliente(clientes):
    print('\n\t..---ELiminar Cliente por DNI---..\n')
    if len(clientes) > 0:
        mostrar_clientes(clientes)
        while True:
            dni = input('\nIngrese el dni a eliminar: ')
            if not dni.isdigit():
                print('\n\t..---Debe ingresar numeros sin puntos---..\n')
            else:
                break
        if dni in clientes:
            del(clientes[dni])
            print('\n\t..---Cliente eliminado correctamente---..\n')
        else:
            print('\n\t..---Resultado---..')
            print('\nCliente inexistente\n')
    else:
        print('\n\t..---Resultado---..')
        print('\nLista de clientes vacia')
def salir():
    print('\n\t..---hasta luego---..')

clientes = {}

while True:
    print("""
        ..---Menú Clientes---..
    
    1.Agregar nuevo cliente
    2.Mostrar todos los clientes
    3.Mostrar cliente por DNI
    4.Eliminar cliente
    5.Salir
    """)
    try:
        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            agregar_cliente(clientes)
        elif opcion == 2:
            mostrar_clientes(clientes)
        elif opcion == 3:
            mostrar_cliente_dni(clientes)
        elif opcion == 4:
            eliminar_cliente(clientes)
        elif opcion == 5:
            salir()
            break
        else:
            print('\n\t..---Opcion invalida---..\n')
    except ValueError:
        print('\n\t..---Opcion invalida---..\n')