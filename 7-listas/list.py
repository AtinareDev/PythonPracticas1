lista_peliculas = ["Batman", "Spiderman",
                   "El Señor de los Anillos", "Harry Potter"]
lista_cantantes = list(("2pac", "Drake", "Jennifer Lopez", "Marc Anthony"))
years = list(range(2020, 2050))
variada = ["Victor", 30, 4.4, True, "Texto"]
print(lista_peliculas)
print(lista_peliculas[1])
print(lista_peliculas[-2])
print(lista_cantantes[1:3])
print(lista_peliculas[1:])
print(lista_peliculas[:2])

# Añadir elementos a una lista
lista_cantantes.append("Alan Walker")
print(lista_cantantes)

# Recorrer lista
for pelicula in lista_peliculas:
    print(f"{lista_peliculas.index(pelicula)+1}. {pelicula}")

# Listas multidimensionales
lista_numeros = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(lista_numeros)
print(lista_numeros[0])
print(lista_numeros[0][1])
