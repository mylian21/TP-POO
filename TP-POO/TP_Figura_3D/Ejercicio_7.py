"""Sistema de Geometría 3D: Diseña un sistema de geometría tridimensional que trabaje con figuras en el
espacio 3D. Debes implementar las siguientes clases:
Punto3D: Una clase que representa un punto en el espacio 3D con coordenadas x, y, y z.
Figura3D: Una clase abstracta que representa una figura tridimensional y define métodos abstractos 
para calcular su volumen y área superficial.
Cubo, Esfera y Cilindro: Subclases de Figura3D que implementan los métodos para calcular el volumen y 
área superficial específicos de cada figura.Crea instancias de estas clases y demuestra cómo 
calcular el volumen y área superficial de diferentes figuras tridimensionales.
Importante: Se deberá escribir un detalle del ejercicio explicando de qué manera lo resolvieron, cómo aplicaron 
los distintos conceptos de la POO."""

from abc import ABC, abstractmethod
import math

class Punto3D:
    def __init__(self, Coord_X, Coord_Y, Coord_Z):
        self.Coord_X = Coord_X
        self.Coord_Y = Coord_Y
        self.Coord_Z = Coord_Z

    def mostrar_coordenadas(self):
        return f"({self.Coord_X}, {self.Coord_Y}, {self.Coord_Z})"


class Figura3D(ABC):

    @abstractmethod    #Parte de la abstracción
    def calcular_volumen(self):
        pass

    @abstractmethod    #Parte de la abstracción
    def calcular_area_superficial(self):
        pass


class Cubo(Figura3D):
    def __init__(self, lado):
        self._lado = lado   #Atributo Encapsulado

    @property
    def lado(self):  #Implementación Encapsulamiento
        return self._lado

    def calcular_volumen(self): #Implementación de la abstracción
        return self.lado ** 3

    def calcular_area_superficial(self): #Implementación de la abstracción
        return 6 * self.lado ** 2


class Esfera(Figura3D):
    def __init__(self, radio):
        self.radio = radio

    def calcular_volumen(self):   #Implementación de la abstracción
        return (4 / 3) * math.pi * self.radio ** 3

    def calcular_area_superficial(self):  #Implementación de la abstracción
        return 4 * math.pi * self.radio ** 2


class Cilindro(Figura3D):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcular_area_superficial(self):
        area_base = math.pi * self.radio ** 2
        area_lateral = 2 * math.pi * self.radio * self.altura
        return 2 * area_base + area_lateral


