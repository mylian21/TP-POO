"""Escribe un programa que intente abrir un archivo que no existe y
utilice un bloque try y except para manejar la excepción de"FileNotFoundError"
"""

try:
#Intentamos abrir un archivo que no existe, con el siguiente código:
    with open("archivo.pdf", "r") as archivo:
        contenido = archivo.read()
        print(contenido)

#Excepción si el archivo no se encuentra:
except FileNotFoundError:
    print("Error: El archivo no existe. Verifica el nombre y la ruta del archivo.")
