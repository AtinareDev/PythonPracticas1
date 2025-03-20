from clases import Coche

mi_coche = Coche("Seat","Leon","Negro","9999abc")

# Detectar tipado del objeto
print(type(mi_coche))
print(isinstance(mi_coche, Coche))


print(mi_coche.marca)
mi_coche.mostrar_info()
mi_coche.encender()
mi_coche.acelerar(50)
mi_coche.frenar(20)
mi_coche.apagar()

# print(mi_coche.__kilometraje) # Atributo privado no accesible directamente
print(mi_coche.get_kilometraje()) # Accediendo al atributo privado mediante el getter
