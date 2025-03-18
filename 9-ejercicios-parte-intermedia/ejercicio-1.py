# Hacer una lista de 8 numeros enteros y realizar las siguientes operaciones:
# # recorrer la lista y mostrarla
# ordenarla y mostrarla
# mostrar longitud
# buscar algun valor (que el usuario pida por teclado)

import random
lista = list(range(0, 8))

for numero in lista:
    print(f"{numero}")
print(lista)

random.shuffle(lista)
print(lista)

lista.sort()
print(lista)

print(len(lista))

buscar = int(input("Ingrese un número para buscar en la lista: "))
if buscar in lista:
    print(
        f"El número {buscar} está en la listan en la posición {lista.index(buscar)}")
else:
    print(f"El número {buscar} no está en la lista")
