# Funciones

def multiplicar(num1,num2):
    mult = num1 * num2
    return mult

def prueba():
    # Retorno de multiples valores
    return "hola",45,[1,2,3]

res = multiplicar(5,3)
print(f'El resultado es: {res}')
res = multiplicar(6,3)
print(f'El resultado es: {res}')
print(f'El resultado es: {multiplicar(4,8)}')

# Imprime todos los valores en una tupla
print(prueba())

# Asigna cada retorno a una variable
c,n,l = prueba()

print(c)
print(n)
print(l)