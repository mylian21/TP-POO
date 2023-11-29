"""Hacer un decorador para verificar las precondiciones antes de ejecutar
una función."""

def verificar_precondiciones(precondicion):
    def funcion_decorador(funcion):
        def wrapper(*args, **kwargs):
            if not precondicion(*args, **kwargs):
                raise ValueError(f"Error de precondición no cumplida para la función {funcion.__name__}")
            return funcion(*args, **kwargs)
        return wrapper
    return funcion_decorador

@verificar_precondiciones(lambda a, b: a >= 0 and b >= 0)
def sumar(a, b):
    return a + b

#Si le doy como parametros numeros, retornará como resultado la suma de esos numeros.
print(sumar(2, 4))


