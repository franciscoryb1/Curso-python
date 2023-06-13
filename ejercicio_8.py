class CuentaBancaria:
    def __init__(self):
        self.saldo = 0
        self.transacciones = []
    def extraccion(self, cantidad):
        self.saldo -= cantidad
        self.transacciones.append(("Extraccion", cantidad))
    def deposito(self, cantidad):
        self.saldo += cantidad
        self.transacciones.append(("Deposito", cantidad))
    def consultar_saldo(self):
        return self.saldo
    def listar_transacciones(self):
        for tipo, cantidad in self.transacciones:
            print(f"{tipo}: ${cantidad:.2f}")

def main():
    cuenta = CuentaBancaria()
    cuenta.deposito(100)
    cuenta.extraccion(50)
    cuenta.deposito(200)
    print(f"Saldo actual: {cuenta.consultar_saldo():.2f}")
    print("Transacciones realizadas:")
    cuenta.listar_transacciones()

main()