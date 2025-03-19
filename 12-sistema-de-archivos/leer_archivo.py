import pathlib

ruta_relativa = pathlib.Path('fichero.txt')
ruta_absoluta = pathlib.Path(
    'F:\\proyectos VSCode Python\\PythonPracticas1\\fichero.txt')
encoding = 'utf-8'


fichero = open(ruta_relativa, 'w', encoding=encoding)

for i in range(0, 10):
    fichero.write(f'Número: {i}\n')
fichero.close()

contenido = ruta_relativa.read_text(encoding=encoding)
print(contenido)
