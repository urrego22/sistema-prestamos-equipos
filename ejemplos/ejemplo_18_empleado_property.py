# ============================================================
# Ejemplo 18: Empleado con @property y salario calculado
# Autora: Sara García
# Descripción: Ejemplo del material de encapsulación sobre
#              propiedades calculadas que se actualizan solas.
# ============================================================

class Empleado:
    def __init__(self, nombre, salario_base, horas_extra=0, tarifa_extra=0):
        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra
        self._tarifa_extra = tarifa_extra

    @property
    def nombre(self):
        return self._nombre

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0:
            raise ValueError("El salario base no puede ser negativo")
        self._salario_base = valor

    @property
    def horas_extra(self):
        return self._horas_extra

    @horas_extra.setter
    def horas_extra(self, valor):
        if valor < 0:
            raise ValueError("Las horas extra no pueden ser negativas")
        self._horas_extra = valor

    @property
    def tarifa_extra(self):
        return self._tarifa_extra

    @tarifa_extra.setter
    def tarifa_extra(self, valor):
        if valor < 0:
            raise ValueError("La tarifa extra no puede ser negativa")
        self._tarifa_extra = valor

    @property
    def salario_total(self):
        """Propiedad calculada: salario base + pago por horas extra."""
        return self._salario_base + (self._horas_extra * self._tarifa_extra)

    def __str__(self):
        return (f"{self._nombre} | Base: ${self._salario_base:,} | "
                f"Extras: {self._horas_extra}h x ${self._tarifa_extra} | "
                f"Total: ${self.salario_total:,}")


# Programa principal
emp = Empleado("Sara Garcia", 2000000, 10, 15000)
print(emp)
print()

# Cambiar horas extra actualiza salario_total automaticamente
emp.horas_extra = 20
emp.tarifa_extra = 20000
print(f"Despues de actualizar horas extra:")
print(emp)
print()

# Validaciones
try:
    emp.salario_base = -500
except ValueError as e:
    print(f"Error: {e}")

try:
    emp.horas_extra = -3
except ValueError as e:
    print(f"Error: {e}")