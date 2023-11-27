"""Vehiculo: Implementar las clases Vehiculo, Coche, Motocicleta y Bicicleta. La clase Vehiculo debe tener 
propiedades como marca, modelo y velocidad_maxima. Cada subclase debe definir sus métodos y atributos 
específicos relacionados con el comportamiento de cada tipo de vehículo."""

class Vehiculo:
    def __init__(self, marca, modelo, color, velocidad_maxima):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.velocidad_maxima=velocidad_maxima

    def arrancar():
        pass


class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima):
        super().__init__(marca, modelo, color, velocidad_maxima)

    def arrancar(self):
        print("El coche arranca cuando se pone en marcha el motor.")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima):
        super().__init__(marca, modelo, color, velocidad_maxima)
    
    def arrancar(self):
        print("La motocicleta arranca cuando se pone en marcha el motor.")    


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad_maxima):
        super().__init__(marca, modelo, color, velocidad_maxima)

    def arrancar(self):
        print("La bicicleta arranca cuando se comieza a pedalear.")  

