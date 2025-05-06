class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

# Uso de la clase
cuenta = CuentaBancaria("Wilson", 1000)
cuenta.depositar(500)
cuenta.mostrar_saldo()

# print(cuenta.__saldo)  # Esto daría error: el atributo es privado
