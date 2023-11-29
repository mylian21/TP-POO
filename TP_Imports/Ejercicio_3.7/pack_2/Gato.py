from .Animal import Animal as Ani

class Gato(Ani):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)

    def info_animal(self): 
        info=super().info_animal()
        return f"{info} Es hermoso"
    