from variables import Datos
class Concatenacion:
    def __init__(self):
        self.variables = Datos()  # Ahora se usa la clase Datos correctamente
        
    def concatenar(self):
        # Concatenar texto de 4  formas
        texto = self.variables.texto
        print("-" * 50)
        print(type(texto))
        print(texto + " Mundo 1")  
        print(texto,"Mundo",2)  
        print(f"{texto} Mundo 3")  # Hola Mundo incrustando variables
        print("{} Mundo {}".format(texto,4))  # Hola Mundo con metodo format
        print("-" * 50)
        
        # Sumar dos enteros
        suma_enteros = self.variables.numero + 10
        print(type(suma_enteros))
        print(suma_enteros)  # 20
        print("-" * 50)
        
        # Sumar dos números decimales
        suma_decimales = self.variables.numero_decimal
        print(type(suma_decimales))
        print(suma_decimales + 10.5)  # 21.0
        print("-" * 50)
        
        # Imprimir valor booleano
        booleano = self.variables.verdadero
        print(type(booleano))
        print(booleano)  # True
        print("-" * 50)
        
        # Sumar listas
        lista = self.variables.lista
        print(type(lista))
        print(lista + [40, 50, 60])  # [10, 20, 30, 40, 50, 60]
        print("-" * 50)
        
        # Sumar tuplas
        tupla = self.variables.tupla
        print(type(tupla))
        print(tupla + (400, 500, 600))  # (100, 200, 300, 400, 500, 600)
        print("-" * 50)
        
        # Imprimir diccionario
        diccionario = self.variables.diccionario
        print(type(diccionario))
        print(diccionario)  # {'nombre': 'Christian', 'apellido': 'Cazorla'}
        print("-" * 50)

        # Cambiar tipo de dato de una variable ( ejemplo de numero a str)
        print(type(suma_enteros))
        print(suma_enteros)
        enteros_string = str(suma_enteros)
        print(type(enteros_string))
        print(enteros_string)
        print("-" * 50)

        # Uso de caracteres de escape
        print("Ella me dijo: \"Asi no\"")
        print ("1 \n2") # salto de linea
        print ("1 \t2") # tabulacion
        print ("1 \r2") # retorno de carro(borra lo anterior)




# Crear una instancia de Concatenacion y llamar al método
concatenacion = Concatenacion()
concatenacion.concatenar()