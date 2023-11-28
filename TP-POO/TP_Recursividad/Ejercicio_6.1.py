"""Escribe una función recursiva para encontrar y sumar todos los números
primos desde 1 hasta un número deseado."""

def num_primo(num, divisor=2):
    if num < 2:
        return False
    if divisor > num // 2:
        return True
    if num % divisor == 0:
        return False
    return num_primo(num, divisor + 1)

def sumar_primos_hasta(num):
    if num < 2:
        return 0
    if num_primo(num):
        return num + sumar_primos_hasta(num - 1)
    else:
        return sumar_primos_hasta(num - 1)

numero_deseado = 5
resultado = sumar_primos_hasta(numero_deseado)
print(f"La suma de los números primos hasta {numero_deseado} es: {resultado}")
