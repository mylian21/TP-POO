"""Hacer un decorador para registrar las llamadas a una función, junto con
sus argumentos y resultados."""

def registro_llamadas(funtion):
    def wrapper(*args, **kwargs):
        print(f"La función es:{funtion.__name__}")
        return funtion(*args,**kwargs)
    return wrapper

@registro_llamadas
def multiplicar(num1, num2):
    return num1*num2

resultado=multiplicar(4,10)
print(resultado)