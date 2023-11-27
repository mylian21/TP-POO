from Empleado import Empleado, Gerente, Trabajador

#Instanciamos los objetos:
gerente=Gerente("Pepe",500.000,"Gerencia General")
print(gerente.mostrar_info())
print(gerente.tipo_empleado())

trabajador=Trabajador("Maria",250.000,"Administración")
print(trabajador.mostrar_info())
print(trabajador.tipo_empleado())