"""Coche: Crear la clase Coche con atributos privados y/o públicos según corresponda de velocidad y kilometraje. 
Definir métodos públicos para acelerar y registrar el kilometraje de manera segura. """

class Coche:
    def __init__(self, velocidad, kilometraje):
        self._velocidad=velocidad
        self._kilometraje=kilometraje

    @property
    def velocidad(self):
        return self._velocidad
    
    @property
    def kilometraje(self):
        return self._kilometraje
    
    def acelerar(self, aumento_velocidad):
        self._velocidad += aumento_velocidad
    
    def registrar_kilometraje(self, kilometraje_recorrido):
        self._kilometraje += kilometraje_recorrido
    
#Instanciamos el objeto:
coche1 = Coche(60, 10)
print("Velocidad:", coche1.velocidad)
print("Kilometraje:", coche1.kilometraje)

coche1.acelerar(50)
print("Velocidad después de acelerar:", coche1.velocidad)

coche1.registrar_kilometraje(20)
print("Kilometraje después de registrar:", coche1.kilometraje)