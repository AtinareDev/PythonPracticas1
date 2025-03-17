# Monto un pequeño bucle siempre activo para el menu

while True:
    print("\nElige un tipo de comparación para mostrar:")
    print("1. Igualdad (==)")
    print("2. Desigualdad (!=)")
    print("3. Mayor que (>)")
    print("4. Menor que (<)")
    print("5. Mayor o igual que (>=)")
    print("6. Menor o igual que (<=)")
    print("7. Operadores lógicos (and, or, not)")
    print("8. Salir")
# el usuario elige que quiere probar
    opcion = input("Ingresa el número de la opción deseada: ")
# tambien puede salir del programa con el 8
    if opcion == "8":
        print("Saliendo del programa...")
        break
# introduce los elementos a probar
    elemento_1 = input("Introduce un elemento: ")
    elemento_2 = input("Introduce otro elemento: ")
# si ambos son digitos se pasan a enteros (ya que por defecto input asigna string a lo que se introduce)
    if elemento_1.isdigit() and elemento_2.isdigit():
        elemento_1 = int(elemento_1)
        elemento_2 = int(elemento_2)
# aqui se revisan los datos
    if opcion == "1":
        print(f"¿{elemento_1} es igual a {elemento_2}? {elemento_1 == elemento_2}")
# != significa que a no es igual a b
    elif opcion == "2":
        print(
            f"¿{elemento_1} es diferente de {elemento_2}? {elemento_1 != elemento_2}")
# > significa que a es mayor que b
    elif opcion == "3":
        print(f"¿{elemento_1} es mayor que {elemento_2}? {elemento_1 > elemento_2}")
# < significa que a es menor que b
    elif opcion == "4":
        print(f"¿{elemento_1} es menor que {elemento_2}? {elemento_1 < elemento_2}")
# >= significa que a es mayor o igual que b
    elif opcion == "5":
        print(
            f"¿{elemento_1} es mayor o igual que {elemento_2}? {elemento_1 >= elemento_2}")
# <= significa que a es menor o igual que b
    elif opcion == "6":
        print(
            f"¿{elemento_1} es menor o igual que {elemento_2}? {elemento_1 <= elemento_2}")
# and significa que a y b son verdaderos
# or significa que a o b son verdaderos
# not significa que a no es verdadero
    elif opcion == "7":
        condicion_1 = elemento_1 == "Antonio"
        condicion_2 = elemento_2 == "Pepe"

        print(
            f"¿{elemento_1} == 'Antonio' and {elemento_2} == 'Pepe'? {condicion_1 and condicion_2}")
        print(
            f"¿{elemento_1} == 'Antonio' or {elemento_2} == 'Pepe'? {condicion_1 or condicion_2}")
        print(f"¿No es '{elemento_1}' igual a 'Antonio'? {not condicion_1}")
# control de fallos
    else:
        print("Opción no válida, intenta de nuevo.")
