"""Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación relativa."""

class Animal:
    def __init__(self, nombre, tipo):
        self.nombre=nombre
        self.tipo=tipo

    def info_animal(self):
        return f"Nombre:{self.nombre}, Tipo:{self.tipo} \n"
        
    def emitir_sonido (self):
        return "El gato maulla"
