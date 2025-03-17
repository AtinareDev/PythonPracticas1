# Importamos la clase Numero desde el archivo 'numeros.py' dentro de la misma carpeta 'operadores'
from numeros import dato_numero

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
    def restar(self):
        # Restamos todos los números de la lista de forma secuencial
        resultado = self.numeros.lista_numeros[0]
        for num in self.numeros.lista_numeros[1:]:
            resultado -= num
        print(f"Resultado de la resta: {resultado}")
        return resultado

    def dividir(self):
        # Dividimos los números de la lista de forma secuencial
        resultado = self.numeros.lista_numeros[0]
        try:
            for num in self.numeros.lista_numeros[1:]:
                resultado /= num  # Dividimos de manera secuencial
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero")
            return None
        print(f"Resultado de la división: {resultado}")
        return resultado

    def maximo(self):
        # Encontramos el máximo número de la lista
        resultado = max(self.numeros.lista_numeros)
        print(f"El número máximo es: {resultado}")
        return resultado

    def minimo(self):
        # Encontramos el mínimo número de la lista
        resultado = min(self.numeros.lista_numeros)
        print(f"El número mínimo es: {resultado}")
        return resultado

    def resto(self):
        # Calculamos el resto de la división secuencial de los números en la lista
        resultado = self.numeros.lista_numeros[0]
        for num in self.numeros.lista_numeros[1:]:
            resultado %= num  # Calculamos el resto de la división
        print(f"Resultado del resto (módulo): {resultado}")
        return resultado