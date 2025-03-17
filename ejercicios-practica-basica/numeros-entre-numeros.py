# programa que muestre todos los numeros entre dos numeros del usuario
# solo los de en medio, no los propios numeros solicitados

elemento1 = int(input("Ingrese el primer número: "))
elemento2 = int(input("Ingrese el segundo número: "))

for numero in range(elemento1+1, elemento2):
    print(numero)
