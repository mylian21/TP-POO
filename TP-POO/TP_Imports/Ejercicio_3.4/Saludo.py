"""Crear dos módulos en el mismo directorio. Desde un módulo, importa
una función o variable del otro utilizando una importación absoluta y
generar un error de importación circular."""

from Responder import responder_saludo

def saludar():
    return "Hola, ¿como estás?"

print(saludar())

