"""Animal: Utilizar la clase Animal del ejercicio de herencia y aplicar polimorfismo para realizar 
el sonido característico del animal. Luego, crear una lista de animales de diferentes tipos y utilizar 
el polimorfismo para hacer que emiten sus sonidos. """

class Animal:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        
    def emitir_sonido (self):
        return "Los animales emiten distintos sonidos según el tipo:"

class Perro(Animal):
    def __init__(self, nombre, edad, cant_patas):
        super().__init__(nombre, edad)
        self.cant_patas=cant_patas
    
    def emitir_sonido(self):
        sonido=super().emitir_sonido()
        return sonido + " El perro ladra."


class Gato(Animal):
    def __init__(self, nombre, edad, forma_ojos):
        sonido=super().__init__(nombre, edad)
        self.forma_ojos=forma_ojos

    def emitir_sonido(self):
        sonido=super().emitir_sonido()
        return sonido + " El gato maúlla."


class Pajaro(Animal):
    def __init__(self, nombre, edad, cant_patas):
        super().__init__(nombre, edad)
        self.cant_patas=cant_patas

    def emitir_sonido(self):
        sonido=super().emitir_sonido()
        return sonido + " El Pajaro silva."
    
class Caballo(Animal):
    def __init__(self, nombre, edad, color_pelaje):
        super().__init__(nombre, edad)
        self.color_pelaje=color_pelaje

    def emitir_sonido(self):
        sonido= super().emitir_sonido()
        return sonido + " Los caballos relinchan."
