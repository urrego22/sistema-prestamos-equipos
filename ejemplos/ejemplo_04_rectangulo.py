# ============================================================
# Ejemplo 4: Clase Rectangulo
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre atributos
#              calculados con @property.
# ============================================================

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        """Area calculada dinamicamente."""
        return self.ancho * self.alto

    @property
    def perimetro(self):
        """Perimetro calculado dinamicamente."""
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        return self.ancho == self.alto

    def __str__(self):
        return f"Rectangulo {self.ancho}x{self.alto} | Area: {self.area} | Perimetro: {self.perimetro}"


# Programa principal
rect1 = Rectangulo(5, 3)
rect2 = Rectangulo(4, 4)

print(rect1)
print(f"Es cuadrado: {rect1.es_cuadrado()}")
print()
print(rect2)
print(f"Es cuadrado: {rect2.es_cuadrado()}")
print()

# Si cambiamos el ancho, area y perimetro se actualizan solos
rect1.ancho = 7
print(f"Despues de cambiar ancho a 7:")
print(rect1)

# El area es solo lectura (no tiene setter)
try:
    rect1.area = 100
except AttributeError as e:
    print(f"Error: no se puede asignar area directamente: {e}")