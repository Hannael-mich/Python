diccionario = {1 : 2, 2 : 3, 3 : 4}
diccionario1 = {4 : 5, 5 : 6}

diccionario.update(diccionario1)
print(diccionario)

diccionario.pop(3)
print(diccionario)

print(diccionario.get(2))

diccionario.clear()
print(diccionario)

diccionario.setdefault(4,5)
print(diccionario)

diccionario2 = diccionario1.copy()

print("Copia del diccionario 1 ", diccionario2)