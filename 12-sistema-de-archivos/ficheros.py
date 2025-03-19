from io import open
import pathlib

ruta_relativa = pathlib.Path('fichero.txt')
ruta_absoluta = pathlib.Path(
    'F:\\proyectos VSCode Python\\PythonPracticas1\\fichero.txt')
encoding = 'utf-8'

# Crear fichero con ruta relativa o absoluta
fichero = open(ruta_relativa, 'w', encoding=encoding)
fichero.write('Hola, soy un fichero de texto')
fichero.close()

# Leer fichero
fichero = open('fichero.txt', 'r', encoding=encoding)
contenido = fichero.read()
fichero.close()

# Escribir en fichero
fichero = open('fichero.txt', 'w', encoding=encoding)
fichero.write('Hola, soy un fichero de texto')
fichero.close()
