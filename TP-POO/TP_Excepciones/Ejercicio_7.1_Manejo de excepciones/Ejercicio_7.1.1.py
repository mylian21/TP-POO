"""Escribe un programa que solicite al usuario dos números y realice
la división de uno por el otro. Utiliza un bloque try y except para
manejar la excepción que ocurre si el segundo número es cero."""

try:
#Creamos las variables que el usuario deberá ingresar:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

#Realizamos la división:
    division = numero1 / numero2

#Imprimimos la división:
    print(f"El resultado de la división es: {division}")

#Excepción para cuando el usuario ingrese cero como segundo número:
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero. Por favor, ingresa un segundo número diferente de cero.")


