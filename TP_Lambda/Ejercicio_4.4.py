"""Toma una lista de números y utiliza map con una función lambda para
calcular la raíz cuadrada de cada número."""

import math 

mi_lista=[2,4,6,8,10,12,14]

raiz_2=list(map(lambda a: math.sqrt(a), mi_lista))

print(raiz_2)