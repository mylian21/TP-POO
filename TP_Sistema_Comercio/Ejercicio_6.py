"""Sistema de Comercio Electrónico Diseña un sistema de comercio electrónico para una tienda en línea. Debes
implementar las siguientes clases:
Producto: Una clase que representa un producto con atributos como nombre, precio, cantidad en stock, etc.
CarritoCompra: Una clase que representa el carrito de compras de un cliente. Debe permitir agregar, eliminar 
y calcular el total de los productos en el carrito.
Cliente: Una clase que representa a un cliente con atributos como nombre, dirección, carrito de compra, etc.
Crea instancias de estas clases y demuestra cómo un cliente puede agregar productos a su carrito, realizar 
una compra y calcular el total.
Importante: Se deberá escribir un detalle del ejercicio explicando de qué manera lo resolvieron, cómo aplicaron 
los distintos conceptos de la POO.
"""

from abc import ABC, abstractmethod
#Creé esta clase abstracta para poder aplicar el pilar de la  POO, Abstracción.
class Producto_Abstracto(ABC):
    
    @abstractmethod 
    def Disminuir_Stock(self): #Esta es la Abstracción
        pass
    @abstractmethod
    def Incrementar_Stock(self): #Esta es la Abstracción
        pass

#Creamos la clase "Producto"
class Producto(Producto_Abstracto):
    def __init__(self, nombre, precio, cantidad_stock, categoria):
        self._nombre=nombre   #Atributo encapsulado
        self._precio=precio    #Atributo encapsulado
        self.cantidad_stock=cantidad_stock
        self.categoria=categoria

    @property   #Decorador para poder acceder al atributo encapsulado
    def nombre(self): 
        return self._nombre

    @property   #Decorador para poder acceder al atributo encapsulado
    def precio(self): 
        return self._precio

    def Disminuir_Stock(self): #Implementación de la abstracción
        if self.cantidad_stock > 0:
            self.cantidad_stock-= 1
  
    def Incrementar_Stock(self): #Implementación de la abstracción
        self.cantidad_stock += 1

    def Info_producto(self): #Polimorfismo
        return f"Nombre:{self._nombre}, Precio: {self.precio}, Cantidad: {self.cantidad_stock}, Categoría: {self.categoria}\n"


#Creamos la clase Carrito tal como lo solicita la consigna, con los métodos mencionados
class Carrito_Compra(Producto): #Herencia
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
    
    def calcular_importe_total(self):
        suma=0
        for producto in self.productos:
            suma += producto.precio
        return suma

    def info_producto(self): #Polimorfismo
        producto=super().Info_producto()
        return f"Usted tiene en el carrito de compras:\n", producto
    
    
#Creamos la clase "Cliente" que tiene un carrito de compras
class Cliente():
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = Carrito_Compra()

    def completar_compra(self):
        total_productos = len(self.carrito.productos)
        return f"Compra completada por {self.nombre} por un total de {total_productos} productos."
    
    
