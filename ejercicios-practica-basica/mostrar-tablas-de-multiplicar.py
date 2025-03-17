# vamos a crear un script que haga todas las tablas de multiplicar hasta el 10 y las muestre por pantalla
tabla = 1
while tabla <= 10:
    print(f"Tabla del {tabla}")
    for numero in range(11):
        print(f"{tabla} x {numero} = {tabla * numero}")
    print("-"*50)
    tabla += 1
