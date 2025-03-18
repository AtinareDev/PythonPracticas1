# Hay una serie de funciones predefinidas en Python

import random
print("Funciones predefinidas en Python")

# detectar tipo de dato
tipo = type(1)
print(tipo)

comprobar = isinstance(1, int)
print(comprobar)

# limpiar espacios de un string
texto = "    hola mundo    "
print(texto)
print(texto.strip())

# borrar variables
year = 2022
print(year)
del year  # borra la variable

# comprobar longitud de una variable
texto = "  "
if len(texto) <= 0:
    print("La variable está vacía")

# encontrar caracteres en un string
frase = "La vida es bella"
print(frase.find("vida"))  # devuelve la posición donde se encuentra

# reemplazar texto en una cadena
nueva_frase = frase.replace("bella", "hermosa")
print(nueva_frase)

# convertir a mayúsculas y minúsculas
print(frase.upper())
print(frase.lower())
print("Hola Mundo".capitalize())  # Primera letra en mayúscula
print("Hola Mundo".title())  # Primera letra de cada palabra en mayúscula
print("HoLa MuNdO".swapcase())  # Invierte mayúsculas y minúsculas

# convertir a lista
elementos = "manzana,pera,uva".split(",")
print(elementos)

# obtener el valor mínimo y máximo de una lista
numeros = [4, 7, 1, 9, 12]
print(min(numeros))
print(max(numeros))

# redondear número
print(round(8.756, 2))  # redondea a 2 decimales

# generar números aleatorios
print(random.randint(1, 10))

# ordenar una lista
elementos.sort()
print(elementos)

# obtener la suma de una lista
print(sum(numeros))
