# ============================================================
# Ejemplo 5: Clase Cuenta
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre métodos que
#              interactúan con atributos y validación en constructor.
# ============================================================

class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        # Validacion en el constructor
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva."
        self._saldo += cantidad
        return f"Deposito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva."
        if cantidad > self._saldo:
            return "Fondos insuficientes."
        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"


# Programa principal
cuenta = Cuenta("Sara Garcia", 1000)

print(cuenta.consultar_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(2000))    # Fondos insuficientes
print(cuenta.depositar(-50))   # Cantidad invalida
print()

# Validacion en constructor
try:
    cuenta_mala = Cuenta("Carlos", -500)
except ValueError as e:
    print(f"Error al crear cuenta: {e}")