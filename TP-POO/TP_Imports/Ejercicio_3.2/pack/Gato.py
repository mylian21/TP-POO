from .Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)

    def info_animal(self): 
        info=super().info_animal()
        return f"{info} Es hermoso"
    