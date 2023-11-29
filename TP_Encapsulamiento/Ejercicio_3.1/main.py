from Cuenta_Bancaria import CuentaBancaria

#Instanciamos el objeto:    
cuenta=CuentaBancaria("Mylian Peña", 200000)
print(cuenta.info_cuenta())
print(cuenta.depositar_dinero(2000))
print(cuenta.retirar_dinero(25000))
print(cuenta.consultar_saldo())
