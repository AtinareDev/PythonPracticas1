# variable local es aquella que se define dentro de una función y solo puede ser utilizado dentro de ella.
# Si se intenta acceder a una variable local desde fuera de la función, se generará un error.
# Por otro lado, una variable global es aquella que se define fuera de una función y puede ser utilizada en cualquier parte del programa.
# En este caso, si se intenta acceder a una variable global desde dentro de una función, se podrá hacer sin problemas.

# Variables globales
año = 2025


def funcion_meses():
    # Variable local
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return meses


# Salida: Estamos en el año 2025 en el mes de Marzo
def imprimir_fecha():
    print(f"Estamos en el año {año} en el mes de {funcion_meses()[2]}")


imprimir_fecha()
