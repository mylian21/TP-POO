"""Hacer un decorador para agrega un retardo antes de que se ejecute
una función."""

#Importamos el módulo "time" que proporciona funciones relacionadas con el tiempo que nos ayude con el retardo.

import time

def agregar_retardo(retardo):
    def ejecucion_funcion(funcion):
        def wrapper(*args,**kwargs):
            time.sleep(retardo) 
            return funcion(*args,**kwargs)
        return wrapper
    return ejecucion_funcion

@agregar_retardo(3) #Usamos el decorador
def multiplicar(a, b):
    return a * b
print("El resultado de multiplicar 2 y 2 es:")
print(multiplicar(2, 2)) #Llamamos a la función del decorador

