from Sonido_animal import Animal, Perro, Gato, Pajaro, Caballo

#Instanciamos los objetos:    
animales=[
    Perro("India", 2, 4,),
    Gato("Chimuelo", 1, "Gatunos"),
    Pajaro("Stuart", 1, 4),
    Caballo("Pepe", 4, "Blanco y Marrón")
]
for animal in animales:
    print(animal.emitir_sonido())
    