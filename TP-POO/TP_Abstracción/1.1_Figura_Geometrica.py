"""FiguraGeometrica: Utilizar clases FiguraGeometrica, Circulo, Rectangulo y Triangulo y que contenga métodos 
y atributos relacionados con el cálculo del área y perímetro de una figura geométrica. Definan los métodos y 
atributos necesarios para calcular el área y el perímetro de cada tipo de figura utilizando los conceptos de abstracción"""

import math

class Figura_Geometrica:
    def __init__ (self, nombre):
        self.nombre=nombre

    def calc_area (self):
        pass

    def calc_perimetro(self):
        pass


class Circulo (Figura_Geometrica):
    def __init__(self, nombre, radio):
        self.radio=radio

    def calc_area (self):
        return math.pi*self.radio**2

    def calc_perimetro(self):
        return 2*math.pi*self.radio


class Rectangulo(Figura_Geometrica):
    def __init__ (self, nombre, base, altura):
        self.base=base
        self.altura=altura

    def calc_area (self):
        return self.base*self.altura

    def calc_perimetro(self):
        return 2*(self.base+self.altura)


class Triangulo(Figura_Geometrica):
    def __init__(self, nombre, base, altura, lado_A, lado_B, lado_C):
        self.base=base
        self.altura=altura
        self.lado_A=lado_A
        self.lado_B=lado_B
        self.lado_C=lado_C

    def calc_area (self):
        return (self.base*self.altura)/2

    def calc_perimetro(self):
        return (self.lado_A+self.lado_B+self.lado_C)

#Instanciamos los objetos:    
circulo=Circulo("circulo", 2)
print ("El área del círculo es: ", circulo.calc_area())
print ("El perímetro del círculo es: ", circulo.calc_perimetro())

rectangulo=Rectangulo("Rectángulo", 5, 7)
print ("El área del rectágulo es: ", rectangulo.calc_area())
print ("El perímetro del rectángulo es: ", rectangulo.calc_perimetro())

triangulo=Triangulo("Triángulo", 4, 6, 4, 7, 5)
print ("El área del triángulo es: ", triangulo.calc_area())
print ("El perímetro del triángulo es: ", triangulo.calc_perimetro())