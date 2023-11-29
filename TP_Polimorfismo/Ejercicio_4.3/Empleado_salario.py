"""Empleado: Utilizar la clase Empleado del ejercicio de herencia y aplicar polimorfismo para calcular el 
salario de acuerdo con las reglas específicas de cada tipo de empleado. Luego, crear una lista de empleados 
de diferentes tipos y utilizar el polimorfismo para calcular sus salarios."""

class Empleado:
    def __init__(self,nombre,salario,departamento, tipo_empleado):
        self.nombre=nombre
        self.salario=salario
        self.departamento=departamento
        self.tipo_empleado=tipo_empleado

    def mostrar_info(self):
        return f"Nombre: {self.nombre} \nSalario: {self.salario} \nDepartamento: {self.departamento} \nCargo del Empleado: {self.tipo_empleado} "
    
    def calc_salario(self):
        return self.salario


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, tipo_empleado, plus_gerente):
        super().__init__(nombre, salario, departamento,tipo_empleado)
        self.plus_gerente=plus_gerente

    def mostrar_info(self):
        return super().mostrar_info()

    def calc_salario(self):
        salario= super().calc_salario()+ self.plus_gerente
        return salario 


class Trabajador(Empleado):
    def __init__(self, nombre, salario, departamento, tipo_empleado, bono_alimenticio):
        super().__init__(nombre, salario, departamento, tipo_empleado)
        self.bono_alimenticio=bono_alimenticio

    def mostrar_info(self):
        return super().mostrar_info()
    
    def calc_salario(self):
        salario= super().calc_salario()
        return salario + self.bono_alimenticio

    
    
