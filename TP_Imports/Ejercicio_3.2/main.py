from pack.Animal import Animal
from pack.Gato import Gato

gatito=Animal("Chimuelo", "Gato")
print(gatito.info_animal())
print(gatito.emitir_sonido())

gatito2=Gato("Rene", "Gatita")
print(gatito2.info_animal())


