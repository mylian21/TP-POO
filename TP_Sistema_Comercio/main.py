from Ejercicio_6 import Producto_Abstracto, Producto, Carrito_Compra, Cliente

#Instanciamos los objetos:
remera= Producto("Remera Azul", 8500 , 500, "Camiseta")
pantalon =Producto("Jean Negro",20000 , 850, "Pantalones")

carrito = Carrito_Compra()
carrito.agregar_producto(remera)
carrito.agregar_producto(pantalon)
print(carrito.calcular_total())
cliente1=Cliente("Mylian Peña", "Balvanera")
cliente1.carrito.agregar_producto(remera)
cliente1.carrito.agregar_producto(pantalon)
print(cliente1.completar_compra())
print(f"Importe total de la compra: $",cliente1.carrito.calcular_importe_total())
