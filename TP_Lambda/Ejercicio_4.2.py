"""Toma una lista de cadenas y utiliza map con una función lambda para
convertir todas las cadenas en mayúsculas."""

mis_sobris=["Fabián", "Martín", "Paulina", "Hassant", "Marcela"]

mayusc=list(map(lambda a: a.upper(), mis_sobris))

print(mayusc)