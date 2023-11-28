"""Solicita al usuario que ingrese una cadena que represente un
número. Utiliza un bloque try y except para manejar la excepción
que se produce si la cadena no se puede convertir a un número."""

try:
#Creamos la variable que el usuario deberá ingresar:
    cadena_numero = input("Ingresa una cadena que represente un número: ")

#Convertimos la cadena a un número
    numero = float(cadena_numero)

#Mostramos el número convertido
    print(f"El número convertido es: {numero}")


#Excepción si la cadena no se puede convertir a un número:
except ValueError:
    print("Error: La cadena ingresada no se puede convertir en número.")


