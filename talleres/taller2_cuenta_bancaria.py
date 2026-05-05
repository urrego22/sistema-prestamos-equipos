# ============================================================
# Taller 2: Encapsulación en Python
# Autora: Sara García
# Descripción: Clase CuentaBancaria con atributos privados
#              y propiedades para controlar el acceso a los datos.
# ============================================================


class CuentaBancaria:

    def __init__(self, titular, saldo=0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            titular (str): Nombre del titular de la cuenta
            saldo (float): Saldo inicial (por defecto 0)
        """
        self._titular = titular   # Atributo protegido
        self._saldo = saldo       # Atributo protegido

    # ----------------------------------------------------------
    # Propiedad titular: solo lectura (no se puede modificar)
    # ----------------------------------------------------------
    @property
    def titular(self):
        """Devuelve el nombre del titular."""
        return self._titular

    # ----------------------------------------------------------
    # Propiedad saldo: lectura y escritura con validación
    # ----------------------------------------------------------
    @property
    def saldo(self):
        """Devuelve el saldo actual."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        """Establece el saldo, pero no permite valores negativos."""
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = nuevo_saldo

    # ----------------------------------------------------------
    # Método depositar
    # ----------------------------------------------------------
    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta.
        Devuelve True si fue exitoso, False si la cantidad no es positiva.
        """
        if cantidad <= 0:
            print("  La cantidad a depositar debe ser positiva.")
            return False
        self._saldo += cantidad
        print(f"  Deposito exitoso. Nuevo saldo: ${self._saldo:,.2f}")
        return True

    # ----------------------------------------------------------
    # Método retirar
    # ----------------------------------------------------------
    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta.
        Devuelve True si fue exitoso, False si no hay saldo suficiente.
        """
        if cantidad > self._saldo:
            print(f"  Saldo insuficiente. Saldo actual: ${self._saldo:,.2f}")
            return False
        self._saldo -= cantidad
        print(f"  Retiro exitoso. Nuevo saldo: ${self._saldo:,.2f}")
        return True

    def __str__(self):
        return (
            f"Titular: {self._titular} | "
            f"Saldo: ${self._saldo:,.2f}"
        )


# ============================================================
# Prueba de la clase CuentaBancaria
# ============================================================
def main():
    # Crear dos cuentas bancarias
    cuenta1 = CuentaBancaria("Sara Garcia", 500000)
    cuenta2 = CuentaBancaria("Carlos Lopez")  # Saldo inicial 0

    print("=== Informacion inicial de las cuentas ===")
    print(cuenta1)
    print(cuenta2)
    print()

    # Depositar dinero
    print("=== Depositos ===")
    cuenta1.depositar(200000)
    cuenta2.depositar(150000)
    print()

    # Intentar depositar una cantidad inválida
    print("=== Deposito invalido ===")
    cuenta1.depositar(-5000)
    print()

    # Retirar dinero
    print("=== Retiros ===")
    cuenta1.retirar(100000)
    print()

    # Intentar retirar más de lo disponible
    print("=== Retiro con saldo insuficiente ===")
    cuenta2.retirar(500000)
    print()

    # Mostrar información final
    print("=== Informacion final de las cuentas ===")
    print(cuenta1)
    print(cuenta2)
    print()

    # Demostrar que titular es solo lectura
    print("=== Propiedad titular (solo lectura) ===")
    print(f"Titular cuenta 1: {cuenta1.titular}")
    try:
        cuenta1.titular = "Otro nombre"  # Esto debe lanzar error
    except AttributeError:
        print("  No se puede modificar el titular (propiedad de solo lectura).")

    # Demostrar validación de saldo negativo
    print()
    print("=== Validacion de saldo negativo ===")
    try:
        cuenta1.saldo = -999
    except ValueError as e:
        print(f"  Error: {e}")


if __name__ == "__main__":
    main()