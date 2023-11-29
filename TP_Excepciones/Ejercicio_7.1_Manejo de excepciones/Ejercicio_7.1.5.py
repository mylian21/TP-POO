"""Crea un diccionario y luego intenta acceder a un valor utilizando
una clave que no está en el diccionario. Utiliza un bloque try y
except para manejar la excepción que se produce si la clave no existe."""

try:
#Creamos un diccionario
    mi_diccionario = {"clave1": "Hola", "clave2": "Hello", "clave3": "Aloha"}

#Creamos la variable que el usuario deberá ingresar:
    clave = input("Ingresa una clave para acceder al diccionario: ")

#Accedemos al valor utilizando la clave ingresada:
    valor = mi_diccionario[clave]

#Imprimos el valor
    print(f"El valor asociado a la clave '{clave}' es: {valor}")

#Excepción si la clave no existe en el diccionario:
except KeyError:
    print(f"Error: La clave '{clave}' no existe en el diccionario.")

