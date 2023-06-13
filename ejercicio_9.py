class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []
    def depositar(self, cantidad):
        self.saldo += cantidad
        self.movimientos.append(("Deposito", cantidad))
    def extraer(self, cantidad):
        if self.saldo < cantidad:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        self.movimientos.append(("Extracción", cantidad))
    def listar_movimientos(self):
        for movimiento in self.movimientos:
            print(f"{movimiento[0]}: {movimiento[1]}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, descubierto=0):
        super().__init__(titular, saldo)
        self.descubierto = descubierto
    def extraer(self, cantidad):
        if self.saldo + self.descubierto < cantidad:
            raise ValueError("Saldo insuficiente")
        if self.saldo < cantidad:
            self.descubierto -= cantidad - self.saldo
            self.saldo = 0
        else:
            self.saldo -= cantidad
        self.movimientos.append(("Extracción", cantidad))

class CajaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0, tasa_interes=0.01):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        self.movimientos.append(("Interes", interes))


cc = CuentaCorriente("Juan", 1000, 500)

# Se depositan $2000 en la cuenta.
cc.depositar(2000)

# Hacer una extracción de 3000 (debería fallar porque excede el descubierto)
try:
    cc.extraer(3000)
except ValueError as e:
    print(str(e)) # Saldo insuficiente

# Se verifica si el importe a extraer es menor que la suma de el saldo y el descubierto, de ser asi, se extrae el valor de la cuenta, caso contrario ocurre un error.
cc.extraer(2500)

# Listar los movimientos de la cuenta corriente.
cc.listar_movimientos()

# Crear una cuenta de caja de ahorro con u saldo de 5000 y una tasa de interes del 2%
ca = CajaAhorro("Maria", 5000, 0.02)

# Se depositan 1000 en la caja de ahorro.
ca.depositar(1000)

# Se aplica el interes ingresado (2%) al saldo de la cuenta.
ca.aplicar_interes()

# Listar los movimientos de la caja de ahorro.
ca.listar_movimientos()