# Un diccionario es un tipo de dato que se utiliza para almacenar múltiples elementos en una sola variable.
# Cada elemento de un diccionario tiene una clave y un valor.
# Los diccionarios no tienen orden.
# No se puede acceder mediante índices, sino mediante claves.
# Los elementos de un diccionario son mutables, pero las claves no lo son.


# Creación de un diccionario
persona = {
    "nombre": "Antonio",
    "apellido": "Pérez",
    "edad": 25
}
print(persona)

# Acceder a un valor específico
print(persona["nombre"])
print(persona["edad"])

# Agregar un nuevo elemento al diccionario
persona["ocupacion"] = "Ingeniero"
print(persona)

# Modificar un valor existente
persona["edad"] = 26
print(persona)

# Eliminar un elemento del diccionario
del persona["apellido"]
print(persona)

# Recorrer el diccionario e imprimir sus elementos
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")
