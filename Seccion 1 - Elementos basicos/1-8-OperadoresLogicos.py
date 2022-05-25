# Operadores Logicos

'''
Operador AND 

se conoce como multiplicacion logica

TRUE = 1
FALSE = 0

 1 x 1 = 1
 1 x 0 = 0

True and True = True
True and False = False
False and True = False
False and False = False

 Operador OR

True or True = True
False or True = True
True or False = True
False or False = False


 Operador Negacion

 not(True) = False
 not(False) = True

 Prioridades

 1 not
 2 And
 3 Or

'''

a = 10
b = 12
c = 13
d = 10

print(((a>b)or(a<c))and((a==c)or(a>=b)))

b = 15
c = 20

resultado = ((a<b) and (b<c))
print(resultado)
resultado = ((a>b) and (b<c))
print(resultado)
resultado = ((a<b) or (b<c))
print(resultado)
resultado = not((a<b) or (b<c))
print(resultado)