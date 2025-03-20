# ValueError
try:
    numero = int(input("Ingrese un número: "))  # Puede lanzar ValueError
    resultado = 10 / numero  # Puede lanzar ZeroDivisionError
except ValueError:
    print("Error: Debes ingresar un número entero.")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
else:  # Se ejecuta si no hay errores
    print(f"El resultado de 10 / {numero} es {resultado}")
finally:  # Se ejecuta siempre, haya o no errores
    print("El programa ha finalizado.")
