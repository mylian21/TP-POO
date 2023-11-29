"""Escribe una función recursiva para calcular el MCD de dos números
enteros."""

def mcd_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)


numero_a = 48
numero_b = 18
result = mcd_recursivo(numero_a, numero_b)
print(f"El MCD de {numero_a} y {numero_b} es: {result}")
