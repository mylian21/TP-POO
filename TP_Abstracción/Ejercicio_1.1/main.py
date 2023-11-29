from Figura_Geometrica import Figura_Geometrica, Circulo, Rectangulo, Triangulo

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