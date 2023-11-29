"""Animal: Utilizar las clases Animal, Perro, Gato y Pájaro. Se debe incluir atributos como nombre y edad. 
Las subclases deben heredar y definir métodos y atributos relacionados con el comportamiento y características 
de cada tipo de animal."""

class Animal:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def info_animal(self):
        return f"Nombre:{self.nombre}, Edad:{self.edad} años"
        
    def emitir_sonido (self):
        pass


class Perro(Animal):
    def __init__(self, nombre, edad, cant_patas):
        super().__init__(nombre, edad)
        self.cant_patas=cant_patas

    def info_animal(self):
        info=super().info_animal()
        return f"{info}, Cantidad de Patas:{self.cant_patas}"
    
    def emitir_sonido(self):
        return "El perro ladra"


class Gato(Animal):
    def __init__(self, nombre, edad, forma_ojos):
        super().__init__(nombre, edad)
        self.forma_ojos=forma_ojos

    def info_animal(self):
        info=super().info_animal()
        return f"{info}, Forma de Ojos:{self.forma_ojos}"

    def emitir_sonido(self):
        return "El gato maúlla"


class Pajaro(Animal):
    def __init__(self, nombre, edad, cant_patas):
        super().__init__(nombre, edad)
        self.cant_patas=cant_patas

    def info_animal(self):
        info=super().info_animal()
        return f"{info}, Cantidad de Patas:{self.cant_patas}"

    def emitir_sonido(self):
        return "El Pajaro silva"
  
    
