# Importación y uso del módulo
# se puede importar tambien from mimodulo import * para usar directamente las funciones
# pero no es recomendable ya que puede haber conflictos de nombres con las funciones de otros módulos
# para importar una funcion concreta se usa from mimodulo import saludo
import mimodulo

# Usar las funciones del módulo
print(mimodulo.saludo('Christian'))
print(mimodulo.calculadora(5, 3, 'suma'))
