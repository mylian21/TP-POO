"""CuentaBancaria: Crear la clase CuentaBancaria con atributos privados y públicos para el saldo y titular. 
Definir métodos para depositar, retirar y consultar el saldo de la cuenta. """

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self._saldo=saldo

    @property
    def saldo(self):
        return self._saldo
    
    def info_cuenta(self):
        return f"Titular de la cuenta: {self.titular}, Saldo de la cuenta: {self._saldo}"   
     
    def depositar_dinero(self, cant_dinero):
        self._saldo +=cant_dinero
        return f"Cantidad depositada= {cant_dinero} y su nuevo saldo es: {self._saldo}"

    def retirar_dinero(self, cant_dinero):
        if cant_dinero >= self._saldo:
            return "Saldo insuficiente, intente con otro monto."
        else:
            self._saldo -=cant_dinero
            return f"Cantidad retirada={cant_dinero} y su nuevo saldo es: {self._saldo}"

    def consultar_saldo(self):
        return f"Su saldo es: {self._saldo}"

#Instanciamos el objeto:    
cuenta=CuentaBancaria("Mylian Peña", 200000)
print(cuenta.info_cuenta())
print(cuenta.depositar_dinero(2000))
print(cuenta.retirar_dinero(25000))
print(cuenta.consultar_saldo())


    