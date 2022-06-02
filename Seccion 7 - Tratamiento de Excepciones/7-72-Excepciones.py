# Excepciones

# Cinco <- Excepcion ValueError

while True:
    try:
        numero = int(input('Digite un numero: '))
        print(f'La suma es: {numero+10}')
    except:
        print('Ha Ocurrido un error')
    else: # Se ejecuta en caso de que no haya ningun tipo de excepcion
        print('Programa finalizado correctamente')
        break
    finally: # Siempre se ejecuta con el try y el except
        print('Iteracion finalizada')
        
print('Programa terminado')