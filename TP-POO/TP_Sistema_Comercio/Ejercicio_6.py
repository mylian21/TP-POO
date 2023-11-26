"""Sistema de Comercio Electrónico Diseña un sistema de comercio electrónico para una tienda en línea. Debes
implementar las siguientes clases:
Producto: Una clase que representa un producto con atributos como nombre, precio, cantidad en stock, etc.
CarritoCompra: Una clase que representa el carrito de compras de un cliente. Debe permitir agregar, eliminar 
y calcular el total de los productos en el carrito.
Cliente: Una clase que representa a un cliente con atributos como nombre, dirección, carrito de compra, etc.
Crea instancias de estas clases y demuestra cómo un cliente puede agregar productos a su carrito, realizar 
una compra y calcular el total.
"""
#Creamos las distintas clases según el enunciado
class Producto:
    def __init__(self, nommbre, precio, cantidad_stock, categoria):
        self._nombre=nommbre
        self._precio=precio
        self.cantidad_stock=cantidad_stock
        self.categoria=categoria

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def Disminuir_Stock(self): 
        if self.cantidad_stock > 0:
            self.cantidad_stock-= 1
  
    def Incrementar_Stock(self):
        self.cantidad_stock += 1

class Carrito_Compra:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def calcular_total(self):
        total_productos = 0
        for producto in self.productos:
            total_productos += 1
        return f"El total de productos que tiene el carrito es: {total_productos}"

class Cliente:
    def init(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = Carrito_Compra()

    def completar_compra(self):
        total = self.carrito.calcular_total()
        print(f"Compra completada por {self.nombre} por un total de ${total}.")
        self.carrito = Carrito_Compra()

remera= Producto("Remera Azul", 8500 , 500, "Camiseta")
pantalon =Producto("Jean Negro",20000 , 850, "Pantalones")

carrito = Carrito_Compra()
carrito.agregar_producto(remera)
carrito.agregar_producto(pantalon)


    
