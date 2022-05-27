# Procedimientos - Funciones Sin Retorno de Valor

def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Sebastian')
saludar('Marlene')

def tabla_multiplicar(num):
    for i in range(1,11):
        print(f'{num}*{i} = {num*i}')

tabla_multiplicar(5)
print()
tabla_multiplicar(3)

