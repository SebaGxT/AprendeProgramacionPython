# Ejercicio 2 - Llenar una lsita con los numeros del 1 al 10, luego modificar los elementos de la lista multiplicandolos por un valor que el usuario digite

lista = list(range(1,11))

print('Lista original\n')

for i in lista:
    print(i,end=' ')

multiplicador = int(input('\n\nIngrese un valor a multiplicar: '))

for i in range(0,10):
    lista[i] *= multiplicador


print('\nLista modificada\n')

for i in lista:
    print(i,end=' ')