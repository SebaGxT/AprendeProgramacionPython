# Pilas - Estructura de datos - no existe una estructura de datos directa en python pero se puede trabajar desde listas
# LIFO - Last In First Out

pila = [1,2,3]

# Agregar elementos al final
pila.append(4)
pila.append(5)

print(pila)

# Sacando elemento elementos por el final
n = pila.pop()
print(f"Elemento sacado {n}")

print(pila)
