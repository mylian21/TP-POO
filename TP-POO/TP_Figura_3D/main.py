from Ejercicio_7 import Punto3D, Figura3D, Cubo, Esfera, Cilindro

#Instanciamos los objetos:
punto = Punto3D(1, 2, 3)
print ("Las coordenadas del punto son: ", punto.mostrar_coordenadas())

cubo = Cubo(5)
print ("El vólumen del cubo es: ", cubo.calcular_volumen())
print ("El área superficial del cubo: ", cubo.calcular_area_superficial())

esfera = Esfera(4)
print ("El vólumen del cubo es: ", esfera.calcular_volumen())
print ("El área superficial del cubo: ", esfera.calcular_area_superficial())

cilindro = Cilindro(3, 6)
print ("El vólumen del cubo es: ", cilindro.calcular_volumen())
print ("El área superficial del cubo: ", cilindro.calcular_area_superficial())