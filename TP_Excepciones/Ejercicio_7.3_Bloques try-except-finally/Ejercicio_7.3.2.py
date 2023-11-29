"""Crea un programa que solicite al usuario dos números y una
operación matemática (suma, resta, multiplicación, división) para
realizar. Utiliza bloques try, except y finally para manejar cualquier
excepción que pueda ocurrir durante la operación y asegurarte
de que los recursos se liberen correctamente."""

def operaciones_matematicas(nro1, nro2, operacion):
    try:
        if operacion == 'Suma':
            resultado = nro1 + nro2
        elif operacion == 'Resta':
            resultado = nro1 - nro2
        elif operacion == 'Multiplicacion':
            resultado = nro1 * nro2
        elif operacion == 'Division':
            resultado = nro1 / nro2
        else:
            raise ValueError("Operación no válida. Por favor, elige entre 'Suma', 'Resta', 'Multiplicacion' o 'Division'.")

        print(f"Resultado de la {operacion}: {resultado}")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"Se produjo una excepción: {e}")

    finally:
        print("Operación completada. Recursos liberados.")

#Solicitamos al usuario dos números y una operación:
try:
    nro1 = float(input("Ingresa el primer número: "))
    nro2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (Suma, Resta, Multiplicacion, Division): ")

#Realizamos la operación de llamando a la función:
    operaciones_matematicas(nro1, nro2, operacion)

except ValueError:
    print("Error: Ingresa números válidos.")

except Exception as e:
    print(f"Se produjo una excepción: {e}")
