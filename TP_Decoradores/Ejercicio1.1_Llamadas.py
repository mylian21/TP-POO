"""Hacer un decorador para registrar las llamadas a una función, junto con
sus argumentos y resultados."""

def registro_llamadas(funcion):
    def wrapper(*args, **kwargs):
        registro.append({
        "función": funcion.__name__,
        "argumentos": args,
        "kwargs": kwargs,    
        "resultado": funcion(*args, **kwargs)
        })
        return funcion(*args,**kwargs)
    return wrapper

@registro_llamadas #mi decorador
def sumar(a, b):
    return a + b
registro = []

#Le paso parametros a mi función, con distintos tipos de dato, ya sea "int", "float" y "string":
sumar(21, 14)
sumar("Hola", " soy mylian")
print(registro)