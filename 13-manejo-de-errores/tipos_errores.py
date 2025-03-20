# class TiposDeErrores:
#     """
#     Clase que contiene métodos para demostrar distintos tipos de errores en Python.
#     """

#     def error_sintaxis(self):
#         # SyntaxError: Error de sintaxis Este error ocurre cuando el código no
#         # sigue las reglas del lenguaje
#         # eval('if True print("Hola")')
#         # pass

#     # def error_nombre(self):
#     #     # NameError: Variable no definida
#     #     return variable_inexistente  # Esta variable no ha sido definida

#     # def error_tipo(self):
#     #     # TypeError: Tipo de dato incorrecto
#     #     return 5 + "10"  # No se puede sumar un entero con una cadena

#     # def error_valor(self):
#     #     # ValueError: Valor incorrecto
#     #     # No se puede convertir una cadena no numérica a entero
#     #     return int("Hola")

#     def error_division(self):
#         # ZeroDivisionError: División por cero
#         return 10 / 0  # No se puede dividir un número entre cero

#     def error_archivo(self):
#         # FileNotFoundError: Archivo no encontrado
#         with open("archivo_inexistente.txt", "r") as file:
#             contenido = file.read()
#         return contenido

#     def error_os(self):
#         # OSError: Error del sistema operativo
#         import os
#         # Intentar eliminar un archivo inexistente
#         os.remove("archivo_que_no_existe.txt")

#     # def error_importacion(self):
#          # ImportError: Error de importación
#           import modulo_inexistente  # Este módulo no existe
