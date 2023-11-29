"""Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación relativa y
utilizar un alias"""

from pack_2.Animal import Animal as Ani
from pack_2.Gato import Gato as Cat

gatito=Ani("Chimuelo", "Gato")
print(gatito.info_animal())
print(gatito.emitir_sonido())

gatito2=Cat("Rene", "Gatita")
print(gatito2.info_animal())

