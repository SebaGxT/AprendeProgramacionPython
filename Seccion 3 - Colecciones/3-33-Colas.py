# Colas
# FIFO - First In First Out

# from collections import deque  -> es lo mismo pero importanto una collection que agrega funciones

cola = ["Maria","Sebastian","Jose","Mario"]

# Agregar Elementos a la cola
cola.append("Alejandro")
cola.append("Carla")
cola.append("Flor")

print(cola)

# Sacando elementos por el principio
n = cola.pop(0)
print(f"Estan atendiendo a {n}")
print(cola)
