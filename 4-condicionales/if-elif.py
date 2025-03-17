
# if evalua una condicion y ejecuta un codigo
# elif evalua otra condicion si la primera no se cumple, si se cumple lo omite
# se usa para evaluar condiciones excluyentes!
# else se ejecuta si ninguna de las anteriores se cumple

numero = int(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
