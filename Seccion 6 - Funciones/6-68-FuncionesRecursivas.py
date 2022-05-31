# Funciones recursivas
# Funcionan de forma iterativa llamandose a si mismas y debe ser importante definir el corte de la misma para no volverse infinita

def cuenta_regresiva(num):
    if num > 0:
        print(num)
        cuenta_regresiva(num-1)
    else:
        print('Booom !!!')

cuenta_regresiva(5)