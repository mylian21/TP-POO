from Coche import Coche
    
#Instanciamos el objeto:
coche1 = Coche(60, 10)
print("Velocidad:", coche1.velocidad)
print("Kilometraje:", coche1.kilometraje)

coche1.acelerar(50)
print("Velocidad después de acelerar:", coche1.velocidad)

coche1.registrar_kilometraje(20)
print("Kilometraje después de registrar:", coche1.kilometraje)