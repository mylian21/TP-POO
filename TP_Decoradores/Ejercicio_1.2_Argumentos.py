"""Hacer un decorador para verificar que los argumentos de una función
sean del tipo correcto."""

#Si quiero verificar que los argumentos de una función sumar() sean números, lo hago de la siguiente manera:

def verificar_argumentos(funcion):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise TypeError("El argumento debe ser un número.")
        return funcion(*args, **kwargs)
    return wrapper

@verificar_argumentos
def sumar(a, b):
    return a + b

#Si le doy como parametros numeros, retornará como resultado la suma de esos numeros.
print(sumar(10, 15))      #--> Imprimirá como resultado 15

#Si le doy parametros de tipo string, retornará el TypeError
print(sumar("1", "2"))    #---> TypeError: El argumento debe ser un número.
