"""Escribe un programa que intente abrir un archivo, leer su
contenido y luego cerrarlo. Utiliza bloques try, except y finally para asegurarte de 
que el archivo se cierre correctamente, incluso si ocurre una excepción durante la lectura."""

mi_archivo = "archivo.txt"

try:
#Intentamos abrir el archivo en modo lectura:
    with open(mi_archivo, 'r') as archivo:
#Intentamos leer el contenido del archivo:
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)

except FileNotFoundError:
    print(f"El archivo '{mi_archivo}' no se encontró.")

except Exception as e:
    print(f"Se produjo una excepción: {e}")

finally:
#Este bloque se ejecutará siempre, independientemente de si ocurre una excepción o no:
    print("Cerrando el archivo...")
