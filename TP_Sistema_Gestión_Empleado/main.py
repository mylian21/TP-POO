from Ejercicio_5 import Persona, Empleado, Gerente, Departamento

#Instanciamos los objetos:
empleado=Gerente("Mylian Peña", 38, 95878147, 1000000, "Gerente", "IT", 200000)
print(f"Sueldo base del gerente:", empleado.consultar_salario())
print(f"Sueldo del gerente post beneficios:" , empleado.calcular_salario())

empleado1=Empleado("Patricia Gonzalez", 28, 34568987, 280000, "Analista QA")

departamento=Departamento()
departamento.agregar_empleado(empleado)
departamento.agregar_empleado(empleado1)
empleado_departamento=departamento.consultar_empleado()
for empleado in empleado_departamento:
    print(empleado.acceder_info())
