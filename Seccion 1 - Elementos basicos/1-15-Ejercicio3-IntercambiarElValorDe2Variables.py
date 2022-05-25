# Ejercicio 3

a = float(input('a -> '))
b = float(input('b -> '))


print(f'valor a {a}')
print(f'valor b {b}')

'''
Version comun
c

c = a
a = b
b = c

'''

# Version python
a , b = b , a

print(f'valor a {a}')
print(f'valor b {b}')