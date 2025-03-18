cantantes = list(("2pac", "Drake", "Jennifer Lopez", "Marc Anthony"))
numeros = list((1, 8, 3, 8, 5, 1, 8, 1))

# ordenar una lista
print(numeros.sort)

# añadir elementos a una lista
cantantes.append("Alan Walker")

# Especificando donde va a ser añadido
cantantes.insert(1, "David Bisbal")

# Eliminar elementos: pop con indice o remove con valor
cantantes.pop(1)
cantantes.remove("Marc Anthony")

# Dar la vuelta a una lista
numeros.reverse()

# Buscar dentro de una lista
print("Drake" in cantantes)

# longitud de una lista
print(len(cantantes))

# Contar elementos
print(cantantes.count("Drake"))

# Conseguir indice
print(cantantes.index("Drake"))

# Unir listas
cantantes.extend(numeros)

print(cantantes)
