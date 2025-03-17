# Importamos la clase Numero desde el archivo 'numeros.py' dentro de la misma carpeta 'operadores'
from operadores.numeros import dato_numero

class Aritmeticos:
    def __init__(self):
        # Creamos una instancia de la clase Numero
        self.numeros = dato_numero()

    def sumar(self):
        # Usamos la función sum() para sumar todos los números en la lista
        resultado = sum(self.numeros.lista_numeros)
        print(f"Resultado de la suma: {resultado}")
        return resultado

    def multiplicar(self):
        # Realizamos la multiplicación de los números de la lista
        resultado = 1
        for num in self.numeros.lista_numeros:
            resultado *= num  # Multiplicamos todos los números en la lista
        print(f"Resultado de la multiplicación: {resultado}")
        return resultado
