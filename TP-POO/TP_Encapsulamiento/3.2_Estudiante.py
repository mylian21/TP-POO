"""Estudiante: Implementar la clase Estudiante con atributos como nombre, edad y calificaciones. 
Utilizar el encapsulamiento para proteger los datos que deban ser protegidos y proporcionar métodos 
públicos para obtener dichos datos. """

class Estudiante():
    def __init__(self, nombre, edad, calificaciones):
        self._nombre=nombre
        self.edad=edad
        self._calificaciones=calificaciones

    @property
    def nombre(self):
        return self._nombre

    @property
    def calificaciones(self):
        return self._calificaciones
    
    def mostrar_informacion(self):
        return f"Nombre: {self._nombre} \nEdad: {self.edad} \nCalificaciones: {self._calificaciones}"
    
#Instanciamos el objeto:
estudiante1 = Estudiante("Mylian Peña", 38, [10, 8, 7, 9])
print(estudiante1.mostrar_informacion())
