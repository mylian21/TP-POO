from Lista_figura import Figura_Geometrica, Circulo, Rectangulo, Triangulo, Cuadrado

#Instanciamos los objetos: 
formas=[
    Circulo("Círculo",4), 
    Rectangulo("Rectángulo",4,6), 
    Triangulo("Triángulo",3,5,3,4,4), 
    Cuadrado("Cuadrado",4,4,4,4)]
for forma in formas:
    print(forma.mostrar_informacion())
    print("El área es:", forma.calc_area())
    print("El perímetro es:", forma.calc_perimetro())