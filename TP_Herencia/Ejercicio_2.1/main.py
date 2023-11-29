from Animal import Animal, Gato, Perro, Pajaro

#Instanciamos los objetos:
perrito=Perro("India", 2, 4)
print(perrito.info_animal())
print(perrito.emitir_sonido())

gatito=Gato("Chimuelo", 1, "gatunos")
print(gatito.info_animal())
print(gatito.emitir_sonido())

pajarito=Pajaro("Stuart", 1, 2)
print(pajarito.info_animal())
print(pajarito.emitir_sonido())
