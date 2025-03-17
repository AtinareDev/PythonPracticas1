# pedimos dos numeros al usuario y mostramos solo los impares que hay entre ellos
elemento1 = int(input("Ingrese el primer número: "))
elemento2 = int(input("Ingrese el segundo número: "))

for numero in range(elemento1+1, elemento2):
    if numero % 2 != 0:
        print(numero)
