"""Hacer un administrador de contexto para notificar eventos al entrar y al
salir de un bloque de código."""

class Notificar_Evento:
    def __init__(self):
        pass

    def __enter__(self):
        print("Entrando al resultado de la suma de dos numeros")
        return self

    def __exit__(self, type, value, traceback):
        print("Saliendo del resultado de la suma de dos numeros")


with Notificar_Evento():
    resultado = 8 + 2
    print(resultado)