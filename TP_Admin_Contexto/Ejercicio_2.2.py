"""Crea un administrador de contexto que permita cambiar el directorio de
trabajo al entrar en un bloque y volver al directorio original al salir."""

class Cambiar_Directorio:
    def __init__(self):
        pass

    def __enter__(self):
        print("Cambiando el directorio de trabajo")
        return self

    def __exit__(self, type, value, traceback):
        print("Volviendo al directorio original")


with Cambiar_Directorio():
    multiplicacion=2*8
    print(f"El resultado de multiplicar 2 y 8, es: {multiplicacion}")
