import math
import random
from datetime import datetime
import os
import sys
import json
import re
import time
from collections import Counter
import itertools
import argparse
import socket
import sqlite3
import shutil
from pathlib import Path


class Utilidades:

    # Función usando el módulo math
    @staticmethod
    def calcular_raiz_cuadrada(numero):
        """
        Calcula la raíz cuadrada de un número utilizando el módulo math.
        """
        return math.sqrt(numero)

    # Función usando el módulo random
    @staticmethod
    def numero_aleatorio_inclusivo(inicio, fin):
        """
        Devuelve un número aleatorio entre 'inicio' y 'fin' (incluyendo ambos extremos).
        """
        return random.randint(inicio, fin)

    # Función usando el módulo datetime
    @staticmethod
    def obtener_fecha_actual():
        """
        Devuelve la fecha actual en formato: Día-Mes-Año (e.g., 19-Marzo-2025).
        """
        return datetime.now().strftime('%d-%B-%Y')

    # Función usando el módulo os
    @staticmethod
    def listar_archivos_directorio(directorio):
        """
        Lista todos los archivos y directorios en la ruta especificada.
        """
        return os.listdir(directorio)

    # Función usando el módulo sys
    @staticmethod
    def obtener_version_python():
        """
        Devuelve la versión de Python que se está utilizando en el sistema.
        """
        return sys.version

    # Función usando el módulo json
    @staticmethod
    def convertir_a_json(objeto):
        """
        Convierte un objeto Python a una cadena JSON.
        """
        return json.dumps(objeto)

    # Función usando el módulo re
    @staticmethod
    def encontrar_numeros_en_texto(texto):
        """
        Encuentra todos los números dentro de una cadena de texto.
        """
        return re.findall(r'\d+', texto)

    # Función usando el módulo time
    @staticmethod
    def dormir_segundos(segundos):
        """
        Detiene la ejecución del programa durante el número de segundos especificado.
        """
        time.sleep(segundos)

    # Función usando el módulo collections (Counter)
    @staticmethod
    def contar_ocurrencias(lista):
        """
        Cuenta las ocurrencias de los elementos en una lista utilizando Counter.
        """
        return Counter(lista)

    # Función usando el módulo itertools
    @staticmethod
    def generar_permutaciones(lista):
        """
        Genera todas las permutaciones posibles de una lista utilizando itertools.
        """
        return list(itertools.permutations(lista))

    # Función usando el módulo argparse
    @staticmethod
    def obtener_argumentos_comando():
        """
        Analiza los argumentos pasados por la línea de comandos usando argparse.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument('nombre', type=str, help='Tu nombre')
        args = parser.parse_args()
        return args.nombre

    # Función usando el módulo socket
    @staticmethod
    def crear_conexion_socket():
        """
        Crea un socket de conexión.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.example.com", 80))
        return s

    # Función usando el módulo sqlite3
    @staticmethod
    def crear_base_datos(nombre_db):
        """
        Crea una base de datos SQLite con el nombre dado.
        """
        conn = sqlite3.connect(nombre_db)
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)')
        conn.commit()
        conn.close()

    # Función usando el módulo shutil
    @staticmethod
    def copiar_archivo(origen, destino):
        """
        Copia un archivo de la ruta 'origen' a la ruta 'destino'.
        """
        shutil.copy(origen, destino)

    # Función usando el módulo pathlib
    @staticmethod
    def verificar_existencia_archivo(ruta):
        """
        Verifica si un archivo o directorio existe en la ruta dada usando pathlib.
        """
        p = Path(ruta)
        return p.exists()


# Ejemplo de uso:
util = Utilidades()

# Ejemplo de cada función:
print(util.calcular_raiz_cuadrada(16))  # Salida: 4.0
# Salida: Un número aleatorio entre 1 y 10
print(util.numero_aleatorio_inclusivo(1, 10))
print(util.obtener_fecha_actual())  # Salida: 19-Marzo-2025
# Lista los archivos en el directorio actual
print(util.listar_archivos_directorio("."))
print(util.obtener_version_python())  # Muestra la versión de Python
# Convierte a JSON
print(util.convertir_a_json({"nombre": "Juan", "edad": 30}))
print(util.encontrar_numeros_en_texto(
    "Tengo 3 manzanas y 5 naranjas"))  # ['3', '5']
util.dormir_segundos(2)  # Pausa de 2 segundos
# Salida: Counter({3: 3, 2: 2, 1: 1})
print(util.contar_ocurrencias([1, 2, 2, 3, 3, 3]))
print(util.generar_permutaciones([1, 2, 3]))  # Genera permutaciones
# Toma argumentos de la línea de comandos
print(util.obtener_argumentos_comando())
print(util.crear_conexion_socket())  # Crea un socket de conexión
util.crear_base_datos("mi_base.db")  # Crea una base de datos SQLite
util.copiar_archivo("archivo_origen.txt",
                    "archivo_destino.txt")  # Copia archivo
# Verifica existencia de archivo
print(util.verificar_existencia_archivo("mi_archivo.txt"))
