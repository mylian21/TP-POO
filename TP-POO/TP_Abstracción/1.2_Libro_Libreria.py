"""Libro: Crear las clases Libro y Libreria. La clase Libro debe incluir atributos como titulo, autor 
y precio. La clase Libreria debe contener una lista de objetos Libro y métodos para calcular el precio 
total de todoslos libros en la librería"""

class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo=titulo
        self.autor=autor
        self.precio=precio

class Libreria(Libro):
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def calcular_precio_total(self):
        total_price = 0
        for libro in self.libros:
            total_price += libro.precio
        return total_price

#Instanciamos el objeto    
libreria = Libreria()
libreria.agregar_libro(Libro("Brida", "Paulo Coelho", 2000))
libreria.agregar_libro(Libro("El Alquimista", "Paulo Coelho", 3500))
libreria.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 4800))
print("El precio total de todos los libros es: ", libreria.calcular_precio_total())
