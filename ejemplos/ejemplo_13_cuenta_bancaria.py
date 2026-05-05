# ============================================================
# Ejemplo 13: CuentaBancaria - Atributos privados
# Autora: Sara García
# Descripción: Ejemplo del material de encapsulación sobre
#              atributos públicos, protegidos y privados.
# ============================================================

class CuentaBancaria:
    tasa_interes = 0.03  # Atributo de clase público

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular           # Público
        self._saldo = saldo_inicial      # Protegido (convencion _)
        self.__pin = pin                 # Privado (name mangling __)

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

    def consultar_saldo(self):
        return f"Saldo de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False


# Programa principal
cuenta = CuentaBancaria("Sara Garcia", 1000, "1234")

# Atributo publico: acceso directo
print(cuenta.titular)

# Atributo protegido: accede pero no se recomienda hacerlo directo
print(cuenta._saldo)

# Validar pin con metodo publico (forma correcta)
print(f"Pin correcto: {cuenta.validar_pin('1234')}")
print(f"Pin incorrecto: {cuenta.validar_pin('0000')}")

# Intentar acceder al atributo privado directamente
try:
    print(cuenta.__pin)
except AttributeError as e:
    print(f"Error: {e}")

# Depositar y consultar
cuenta.depositar(500)
print(cuenta.consultar_saldo())