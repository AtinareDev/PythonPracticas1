# Definición del módulo mimodulo.py
def saludo(nombre):
    return f'Hola {nombre}'


def calculadora(numero1, numero2, operacion):
    if operacion == 'suma':
        return numero1 + numero2
    elif operacion == 'resta':
        return numero1 - numero2
    elif operacion == 'multiplicacion':
        return numero1 * numero2
    elif operacion == 'division':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return 'Error: División por cero'
    else:
        return 'Operación no permitida'
