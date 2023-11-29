"""Escribe una función que sume los dígitos de un número pares de un
número entero. Si el número es impar, restarle 3 y sumarlo. Si el número
da negativo, sumar 1."""

def sumar_digitos(numero):
    if numero % 2 == 0 and numero > 0:
# En caso de que sea un numero par le suma los pares
        suma_pares = sum(int(digito) for digito in str(numero) if int(digito) % 2 == 0)
        return suma_pares
# Si el resultado es impar, restar 3 y sumarlo.    
    elif numero % 2 == 1 and numero > 0:
        total=(numero-3)+numero
        return total
# Si el resultado es negativo, sumar 1
    elif numero < 0:
        numneg = numero + 1
        return numneg
    
resultado1 = sumar_digitos(2468)
print(f"Resultado 1: {resultado1}")  #Imprime: 20

resultado2 = sumar_digitos(7)
print(f"Resultado 2: {resultado2}")  #Imprime: 11

resultado3= sumar_digitos(-4)
print(f"Resultado 3: {resultado3}") 
