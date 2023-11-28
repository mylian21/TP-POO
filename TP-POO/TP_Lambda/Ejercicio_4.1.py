"""Dada una lista de números, utiliza map y una función lambda para crear
una nueva lista que contenga el doble de cada número."""

mi_lista=[2,4,6,8,10,12,14]

doble=list(map(lambda a: a*2, mi_lista))

print(doble)