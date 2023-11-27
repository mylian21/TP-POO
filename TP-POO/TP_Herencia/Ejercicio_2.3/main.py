from Forma import Forma, Circulo, Rectangulo

#Instanciamos los objetos:    
circulo=Circulo("circulo", 2)
print ("El área del círculo es: ", circulo.calc_area())
print ("El perímetro del círculo es: ", circulo.calc_perimetro())

rectangulo=Rectangulo("Rectángulo", 5, 7)
print ("El área del rectágulo es: ", rectangulo.calc_area())
print ("El perímetro del rectángulo es: ", rectangulo.calc_perimetro())