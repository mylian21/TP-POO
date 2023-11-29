"""Dada una lista de cadenas, utiliza map y una función lambda para crear
una lista con la longitud de cada palabra."""

mis_sobris=["Fabián", "Martín", "Paulina", "Hassant", "Marcela"]

long=list(map(lambda a: len(a), mis_sobris))

print(long)