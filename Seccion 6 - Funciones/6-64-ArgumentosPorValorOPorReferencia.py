# Argumentos por valor o por referencia

def doblar_valor(numero):
    numero *= 2
    print(numero)

def doblar_valor2(numero):
    return numero*2

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = 5

# Argumento por valor - pasa una copia del valor de n 
doblar_valor(n)
print(n)

# Argumento por valor modificando el valor original
n = doblar_valor2(n)
print(n)

# Todas las colecciones se pasan por argumentos por referencia - modifican directamente el valor de la coleccion tomando su posicion en memoria
n = [5,10,15,20]
doblar_valores(n)
print(n)

# pase por valor una coleccion sin modificar la original
n = [10,15,20,25]
doblar_valores(n[:])
print(n)