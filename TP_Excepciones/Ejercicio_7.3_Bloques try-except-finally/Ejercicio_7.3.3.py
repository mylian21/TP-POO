"""Escribe un programa que abra un archivo, lea su contenido y
escriba el mismo contenido en otro archivo. Utiliza bloques try,
except y finally para manejar cualquier excepción que pueda
ocurrir durante la lectura o escritura, y asegúrate de que ambos
archivos se cierren correctamente."""

def copiar_contenido(origen, destino):
    try:
        with open(origen, 'r') as archivo_origen:       
            contenido = archivo_origen.read()

            with open(destino, 'w') as archivo_destino:           
                archivo_destino.write(contenido)

    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no se encontró.")

    except Exception as e:
        print(f"Se produjo una excepción: {e}")

    finally:
        print("Cerrando archivos.")

#Solicitamos al usuario los nombres de los archivos:
try:
    archivo_origen = input("Ingresa el nombre del archivo de origen: ")
    archivo_destino = input("Ingresa el nombre del archivo de destino: ")

#Realizamos la copia de llamando a la función:
    copiar_contenido(archivo_origen, archivo_destino)

except Exception as e:
    print(f"Se produjo una excepción: {e}")
