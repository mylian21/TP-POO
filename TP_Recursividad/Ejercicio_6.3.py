"""Escribe una función recursiva para invertir una cadena."""

def invertir_cadena(cadena):
# Si la cadena es vacía o tiene un solo carácter, ya estaría invertida
    if len(cadena) <= 1:
        return cadena
    else:
#Invertir la cadena excluyendo el primer y último carácter
        return cadena[-1] + invertir_cadena(cadena[1:-1]) + cadena[0]


cadena_original = "Chimuelo, el gato más HERMOSO, TE AMO!"
cadena_invertida = invertir_cadena(cadena_original)
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {cadena_invertida}")
