class Coche:
    def __init__(self, marca, modelo, color, matricula):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.matricula = matricula
        self.__kilometraje = 5000  # Atributo privado
        self.encendido = False
        self.velocidad = 0

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El coche ha sido encendido.")
        else:
            print("El coche ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            print("El coche ha sido apagado.")
        else:
            print("El coche ya está apagado.")

    def acelerar(self, incremento):
        if self.encendido:
            self.velocidad += incremento
            print(f"El coche ha acelerado a {self.velocidad} km/h.")
        else:
            print("No puedes acelerar un coche apagado.")

    def frenar(self, decremento):
        if self.encendido and self.velocidad > 0:
            self.velocidad = max(0, self.velocidad - decremento)
            print(f"El coche ha frenado a {self.velocidad} km/h.")
        else:
            print("El coche ya está detenido o apagado.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Matrícula: {self.matricula}, "
              f"Encendido: {'Sí' if self.encendido else 'No'}, Velocidad: {self.velocidad} km/h, "
              f"Kilometraje: {self.__kilometraje} km")

    # Métodos getter y setter para el atributo privado __kilometraje
    def get_kilometraje(self):
        return self.__kilometraje

    def set_kilometraje(self, kilometraje):
        if kilometraje >= 0:
            self.__kilometraje = kilometraje
        else:
            print("El kilometraje no puede ser negativo.")
