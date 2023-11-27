"""Empleado: Crear las clases Empleado, Gerente y Trabajador. Se debe tener atributos como nombre, salario
 y departamento. Las subclases deben heredar y definir los métodos y atributos necesarios para representar 
 cada tipo de empleado. """

class Empleado:
    def __init__(self,nombre,salario,departamento):
        self.nombre=nombre
        self.salario=salario
        self.departamento=departamento

    def mostrar_info(self):
        pass
    
    def tipo_empleado(self):
        pass


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento ):
        super().__init__(nombre, salario, departamento)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}") 
        print(f"Departamento: {self.departamento}")

    def tipo_empleado(self):
        return "Tipo de empleado: Gerente"


class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento ):
        super().__init__(nombre, salario, departamento)

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}") 
        print(f"Departamento: {self.departamento}")

    def tipo_empleado(self):
        return "Tipo de empleado: Trabajador"
    
