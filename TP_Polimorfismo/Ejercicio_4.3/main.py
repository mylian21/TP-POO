from Empleado_salario import Empleado, Gerente, Trabajador

#Instanciamos los objetos:
empleado=[Gerente("Krisstel Sanabria", 700000, "Administración", "Gerente", 150000),
          Trabajador("Nicolás Sanchez", 300000, "Administración", "Analista Contable", 100000),
          Gerente("Mylian Peña", 780000, "Tecnología", "Gerente de Proyectos", 150000),
          Trabajador("Ana Beltrán", 380000, "Tecnología", "Analista de Testeo", 100000)
          ]
for empleados in empleado:
    print(empleados.mostrar_info())
    print(f"El sueldo total es:", empleados.calc_salario())