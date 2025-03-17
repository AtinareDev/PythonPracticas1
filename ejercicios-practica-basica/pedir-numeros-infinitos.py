# Pedir numeros infinitamente al usuario hasta que no acierte el que es
while True:
    numero_bingo = 7
    numero = int(input("Ingrese un número del 1 al 7: "))
    if numero == numero_bingo:
        print("¡Bingo! ¡Has acertado!")
        break
    else:
        print("¡Vuelve a intentarlo!")
