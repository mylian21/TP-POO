"""Sistema de Gestión de Personal: Diseña un sistema de gestión de personal para una empresa. 
Debes implementar las siguientes clases: Persona: Una clase base que representa a una persona con atributos 
como nombre, edad y DNI. Utiliza el encapsulamiento para proteger los datos sensibles.
Empleado: Una subclase de Persona que agrega atributos como salario y cargo. Implementa el cálculo 
del salario en base al cargo y permite consultar el salario.
Gerente: Una subclase de Empleado que agrega atributos específicos de un gerente, como departamento.
Departamento: Una clase que contiene una lista de empleados y métodos para agregar, eliminar y consultar empleados.
Crea instancias de estas clases y demuestra cómo agregar empleados a un departamento, calcular salarios 
y acceder a la información de las personas
Importante: Se deberá escribir un detalle del ejercicio explicando de qué manera lo resolvieron, cómo aplicaron 
los distintos conceptos de la POO."""

class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre=nombre        #Parte de Encapsulamiento
        self.edad=edad
        self._dni=dni              #Parte de Encapsulamiento

    @property
    def nombre(self):              #Parte de Encapsulamiento
        return self._nombre 
    @property
    def dni(self):                 #Parte de Encapsulamiento
        return self._dni 

    def acceder_info(self):        #Esta es la Abstracción
        pass


class Empleado(Persona):             #Esto es Herencia
    def __init__(self, _nombre, edad, _dni, salario, cargo):
        super().__init__(_nombre, edad, _dni) 
        self._salario=salario      #Parte de Encapsulamiento
        self.cargo=cargo
    
    @property 
    def salario(self):              #Parte de Encapsulamiento
        return self._salario 
    
    def acceder_info(self):         #Implementación de la abstracción
        return f"Empleado: {self._nombre}, Edad:{self.edad}, DNI:{self._dni}, Salario:{self._salario}, Cargo:{self.cargo}"
    
    def calcular_salario(self):     #Esto es polimorfismo
        if self.cargo == "Presidente":
            return (self._salario*0.40)+self._salario
        
        elif self.cargo == "Gerente":
            return (self._salario*0.30)+self._salario      
        
        elif self.cargo == "Coordinador":
            return (self._salario*0.20)+self._salario

        elif self.cargo == "Analista":
            return (self._salario*0.15)+self._salario

        elif self.cargo == "Asistente":
            return (self._salario*0.10)+self._salario
        else:
            return "No contamos con ese cargo en la empresa"    

    def consultar_salario(self):
        if self.cargo == "Presidente":
            return self._salario 
               
        elif self.cargo == "Gerente":
            return self._salario            
        
        elif self.cargo == "Coordinador":
            return self._salario

        elif self.cargo == "Analista":
            return self._salario

        elif self.cargo == "Asistente":
            return self._salario
        else:
            return "No contamos con ese cargo en la empresa"  
        

class Gerente (Empleado):                 #Esto es Herencia
    def __init__(self, _nombre, edad, _dni, salario, cargo, departamento, plus_alimentación):
        super().__init__(_nombre, edad, _dni, salario, cargo)
        self.plus_alimentación=plus_alimentación
        self.departamento=departamento

    def calcular_salario(self):           #Implementación del polimorfismo
        if self.cargo == "Gerente":
            sueldo=super().calcular_salario()+self.plus_alimentación
            return sueldo
        else:
            return "El empleado no es gerente"       


class Departamento:
    def __init__(self):
        self._empleados = []

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        self._empleados.remove(empleado)

    def consultar_empleado(self, dni):
        for empleado in self._empleados:
            if empleado.dni == dni:
                return empleado
        return "No tenemos un empleado con ese DNI."


empleado=Gerente("PEPE", 38, 95878145, 100000, "Gerente", "IT", 20000)
print(empleado.calcular_salario())
print(empleado.consultar_salario())

empleado1=Empleado("Mylian", 38, 95878147, 280000, "Asistente")
print(empleado1.acceder_info())

departamento=Departamento()
departamento.agregar_empleado(empleado1)
print(departamento.consultar_empleado(95878147))