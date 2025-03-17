# for variable in elemento iterable (lista, rango, etc)

# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]

# Usamos enumerate() para obtener índice y valor
for indice, numero in enumerate(numeros):
    print(f"En la posición {indice} está el número {numero} ")


for numero in range(0, 10):
    print(numero)
