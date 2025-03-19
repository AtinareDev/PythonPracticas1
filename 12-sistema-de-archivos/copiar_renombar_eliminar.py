import shutil
import pathlib
import os.path

# Va a dar error si no he creado el fichero.txt en el directorio en la clase leer_archivo.py
ruta_relativa = pathlib.Path('fichero.txt')
ruta_absoluta = pathlib.Path(
    'F:\\proyectos VSCode Python\\PythonPracticas1\\fichero.txt')
encoding = 'utf-8'
ruta_nueva = 'F:\\proyectos VSCode Python\\PythonPracticas1\\fichero_copiado.txt'

# copiar_archivo(origen, destino)
shutil.copy(ruta_relativa, ruta_nueva)

# renombrar_archivo(origen, destino)
shutil.move(ruta_nueva, 'fichero_renombrado.txt')

# comprobar_existencia_archivo(ruta)
if os.path.exists('fichero_renombrado.txt'):
    print('El archivo existe')
else:
    print('El archivo no existe')

# eliminar_archivo(ruta). Lo comento para que no se ejecute
# os.remove('fichero.txt')
# os.remove('fichero_renombrado.txt')
# print('Archivos eliminados')
