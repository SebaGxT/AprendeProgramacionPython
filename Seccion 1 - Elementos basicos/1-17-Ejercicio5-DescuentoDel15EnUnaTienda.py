importetotal = float(input('Digite el precio del producto: '))
descuento = importetotal * 0.15
res = importetotal - descuento

print(f'El precio final es: ${res:.2f}')