# set es un tipo de dato que se utiliza para almacenar múltiples elementos en una sola variable.
# Un set no puede tener elementos duplicados.
# No tienen orden.
# No se puede acceder mediante índices.
# Los elementos de un set son inmutables, pero el set en sí no lo es.

personas = {"Antonio", "Pepe", "Luis"}
print(personas)

# Añadir elementos a un set
personas.add("Ana")
print(personas)

# Eliminar elementos de un set
personas.remove("Pepe")
print(personas)
