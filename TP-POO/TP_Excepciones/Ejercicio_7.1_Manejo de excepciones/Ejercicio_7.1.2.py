"""Crea una lista de números y, a continuación, intenta acceder a un elemento en un 
índice especificado por el usuario. Utiliza un bloque try y except para manejar la 
excepción que se produce si el índice está fuera de rango."""

try:

#Crear la lista de números:
    numeros = [2, 4, 6, 8, 10, 12, 14, 16]

#Creamos la variable que el usuario deberá ingresar:
    posicion = int(input("Ingresa una posición de la lista, para conocer qué numero está en esa posición: "))

#Accedemos al elemento en la posición especificada:
    elemento = numeros[posicion]

#Mostramos la posición:
    print(f"El número que está en la posición {posicion} de la lista de numeros es: {elemento}")

#Excepción si la posición ingresada está fuera de rango:
except IndexError:
    print("Error: La posición ingresada está fuera de rango. Ingresa una posición válida.")

