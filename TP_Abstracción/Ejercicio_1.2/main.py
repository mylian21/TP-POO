from Libro_Libreria import Libro, Libreria

#Instanciamos el objeto    
libreria = Libreria()
libreria.agregar_libro(Libro("Brida", "Paulo Coelho", 2000))
libreria.agregar_libro(Libro("El Alquimista", "Paulo Coelho", 3500))
libreria.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 4800))
print("El precio total de todos los libros es: ", libreria.calcular_precio_total())