"""Hacer un decorador para verificar que los argumentos de una función
sean del tipo correcto."""

def verificar(funtion):
    def wrapper(*args, **kwargs):
        return funtion(*args,**kwargs)
    return wrapper

@verificar
def multiplicar(num1, num2):
    return num1*num2

resultado=multiplicar(4,10)
print(resultado)