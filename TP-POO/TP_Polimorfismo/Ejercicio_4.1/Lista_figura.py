"""FiguraGeometrica: Utilizar la clase FiguraGeometrica del ejercicio de abstracción y crear un método 
muestre información específica de la figura utilizando polimorfismo. Luego, crear una lista de figuras
geométricas de diferentes tipos y utilizar el polimorfismo para imprimir su información."""

import math

class Figura_Geometrica:
    def __init__ (self, nombre):
        self.nombre=nombre

    def mostrar_informacion (self):
        return f"Información de la figura:{self.nombre}"


class Circulo (Figura_Geometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio=radio

    def calc_area (self):
        return math.pi*self.radio**2

    def calc_perimetro(self):
        return 2*math.pi*self.radio
    
    def mostrar_informacion(self):
        info=super().mostrar_informacion()
        return info + f" Radio: {self.radio}"


class Rectangulo(Figura_Geometrica):
    def __init__ (self, nombre, base, altura):
        super().__init__(nombre)
        self.base=base
        self.altura=altura

    def calc_area (self):
        return self.base*self.altura

    def calc_perimetro(self):
        return 2*(self.base+self.altura)
    
    def mostrar_informacion(self):
        info=super().mostrar_informacion()
        return info + f" Base: {self.base} \nAltura: {self.altura}"

class Triangulo(Figura_Geometrica):
    def __init__(self, nombre, base, altura, lado_A, lado_B, lado_C):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
        self.lado_A=lado_A
        self.lado_B=lado_B
        self.lado_C=lado_C

    def calc_area (self):
        return (self.base*self.altura)/2

    def calc_perimetro(self):
        return (self.lado_A+self.lado_B+self.lado_C)
    
    def mostrar_informacion(self):
        info=super().mostrar_informacion()
        return info + f" Base: {self.base} \nAltura: {self.altura} \nLados: {self.lado_A, self.lado_B, self.lado_C}"

class Cuadrado (Figura_Geometrica):
    def __init__ (self, nombre, lado_A, lado_B, lado_C, lado_D):
        super().__init__(nombre)
        self.lado_A=lado_A
        self.lado_B=lado_B
        self.lado_C=lado_C
        self.lado_D=lado_D

    def calc_area (self):
        return self.lado_A*self.lado_B

    def calc_perimetro(self):
        return (self.lado_A+self.lado_B+self.lado_C+self.lado_D)
    
    def mostrar_informacion(self):
        info=super().mostrar_informacion()
        return info + f" Lados:{self.lado_A, self.lado_B, self.lado_C, self.lado_D}"


