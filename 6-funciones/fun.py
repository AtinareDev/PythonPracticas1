def funcion_1(numero, letra):
    print(f"El número es {numero} y la letra es {letra}")

# para definir un parametro opcional se le asigna un valor por defecto


def funcion_2(numero, parametro_opcional=1):
    print(
        f"El número es {numero} y el parámetro opcional es {parametro_opcional}")


def funcion_3(nombre, apellido):
    nombre_completo = nombre + " " + apellido
    return nombre_completo


def funcion_4(saludo="Hola, "):
    print(f"{saludo}{funcion_3("Antonio", "Pérez")}")


# las funciones lambda son funciones anónimas que se pueden utilizar para funciones simples
# lambda parametros: expresion  (no se necesita return)
# en este caso se crea una función que suma dos números
def suma(a, b): return a + b


resultado = suma(3, 5)
print(resultado)  # Salida: 8


funcion_1(7, "a")
funcion_2(7)
funcion_4()
funcion_4("Buenos dias ")
