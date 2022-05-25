# Condicionales Combinados

edad = int(input("Ingrese su edad: "))

# if edad > 0 and edad < 140
# En python no existe el condicional multiple switch

if  0 < edad < 140:
    if edad >= 18:
        print('Es mayor de edad')
    else:
        print('Es menor de edad')
else:
    print('Edad Incorrecta')