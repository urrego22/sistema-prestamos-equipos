# ============================================================
# Ejemplo 8: Clase Temperatura
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre propiedades
#              @property con getter y setter.
# ============================================================

class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Obtiene la temperatura en Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        """Establece la temperatura en Celsius con validacion."""
        if valor < -273.15:
            raise ValueError("La temperatura no puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Obtiene la temperatura en Fahrenheit (calculada)."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        """Establece la temperatura desde Fahrenheit."""
        self.celsius = (valor - 32) * 5/9


# Programa principal
temp = Temperatura(25)

print(f"{temp.celsius}C = {temp.fahrenheit}F")

temp.celsius = 30
print(f"{temp.celsius}C = {temp.fahrenheit}F")

temp.fahrenheit = 68
print(f"{temp.celsius}C = {temp.fahrenheit}F")

temp.celsius = 0
print(f"Punto de congelacion: {temp.celsius}C = {temp.fahrenheit}F")

temp.celsius = 100
print(f"Punto de ebullicion: {temp.celsius}C = {temp.fahrenheit}F")

# Validacion: temperatura imposible
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")