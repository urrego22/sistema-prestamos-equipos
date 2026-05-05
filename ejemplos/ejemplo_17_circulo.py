# ============================================================
# Ejemplo 17: Circulo con @property de solo lectura
# Autora: Sara García
# Descripción: Ejemplo del material de encapsulación sobre
#              propiedades de solo lectura (sin setter).
# ============================================================

import math

class Circulo:
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser positivo")
        self._radio = valor

    @property
    def area(self):
        """Propiedad de solo lectura: calculada a partir del radio."""
        return round(math.pi * self._radio ** 2, 2)

    @property
    def perimetro(self):
        """Propiedad de solo lectura: calculada a partir del radio."""
        return round(2 * math.pi * self._radio, 2)

    def __str__(self):
        return f"Circulo r={self._radio} | Area={self.area} | Perimetro={self.perimetro}"


# Programa principal
c = Circulo(5)
print(c)
print(f"Radio: {c.radio}")
print(f"Area: {c.area}")
print(f"Perimetro: {c.perimetro}")
print()

# Cambiar radio actualiza area y perimetro automaticamente
c.radio = 10
print(f"Nuevo radio: {c.radio}")
print(c)
print()

# Intentar asignar area directamente (solo lectura)
try:
    c.area = 100
except AttributeError as e:
    print(f"Error: no se puede modificar area directamente.")

# Intentar radio negativo
try:
    c.radio = -3
except ValueError as e:
    print(f"Error: {e}")