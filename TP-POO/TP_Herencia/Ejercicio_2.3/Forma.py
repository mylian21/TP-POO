"""Forma: Implementar las clases Forma, Circulo y Rectangulo. La o las clases deben contener atributos como color
 y dimensiones. Las subclases deben heredar y definir métodos y atributos para calcular el área y el perímetro de 
 cada forma."""

import math
class Forma:
    def __init__(self, color, dimensiones):
        self.color= color
        self.dimensiones= dimensiones

    def calc_area (self):
        pass

    def calc_perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self,color, dimensiones, radio):
        super().__init__(self,color, dimensiones)
        self.radio=radio

    def calc_area (self):
        return math.pi*self.radio**2

    def calc_perimetro(self):
        return 2*math.pi*self.radio

class Rectangulo(Forma):
    def __init__(self, color, dimensiones, base, altura):
        super().__init__(color, dimensiones)
        self.base=base
        self.altura=altura

    def calc_area (self):
        return self.base*self.altura

    def calc_perimetro(self):
        return 2*(self.base+self.altura)    
    
