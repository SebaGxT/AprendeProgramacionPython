# Ejercicio 3 - Menu Para Clientes

def agregar_cliente(clientes):
    print('\nAgregar cliente\n')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    while True:
        dni = input('Ingrese el dni: ')
        if not dni.isdigit():
            print('\nDebe ingresar numeros sin puntos\n')
        else:
            break
    clientes[dni] = {nombre:apellido}
def mostrar_clientes(clientes):
    if len(clientes) > 0:
            for i in clientes:
                print(f'DNI: {i} - Nombre y Apellido:{clientes[i]}')
    else:
        print('\nLista de clientes vacia')
def mostrar_cliente_dni(clientes):
    if len(clientes) > 0:
        while True:
            dni = input('Ingrese el dni: ')
            if not dni.isdigit():
                print('\nDebe ingresar numeros sin puntos\n')
            else:
                break
        cliente = clientes.get(dni,"Dni inexistente")
        if cliente != 'Dni inexistente':
            print(f'DNI: {dni} - Nombre y Apellido: {cliente}')
        else:
            print('Dni inexistente\n')
    else:
        print('\nLista de clientes vacia')
def eliminar_cliente(clientes):
    if len(clientes) > 0:
        mostrar_clientes(clientes)
        while True:
            dni = input('\nIngrese el dni a eliminar: ')
            if not dni.isdigit():
                print('\nDebe ingresar numeros sin puntos\n')
            else:
                break
        if dni in clientes:
            del(clientes[dni])
            print('\nCliente eliminado correctamente\n')
        else:
            print('\nCliente inexistente\n')
    else:
        print('\nLista de clientes vacia')
def salir():
    print('\nhasta luego')

clientes = {}

while True:
    print("""
        Menú Clientes
    
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
            print('\nOpcion invalida\n')
    except ValueError:
        print('\nOpcion invalida\n')