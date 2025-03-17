nombre = "Christian"
ciudad = "Málaga"
edad = 34
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad.")
    if edad >= 65:
        print("Es una persona jubilada.")
    elif edad >= 30:
        print("Es adulto viejuno.")
    else:
        print("Es un adulto joven.")
else:
    print(f"{nombre} es menor de edad.")
    if edad < 13:
        print("Es un niño.")
    else:
        print("Es un adolescente.")

print(f"Hola, me llamo {nombre}, vivo en {ciudad} y tengo {edad} años.")
