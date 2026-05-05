# ============================================================
# Ejemplo 11: Clase Punto
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre métodos
#              especiales (dunder): __str__, __add__, __eq__, __len__.
# ============================================================

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Representacion amigable para el usuario."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Representacion detallada para desarrolladores."""
        return f"Punto({self.x}, {self.y})"

    def __add__(self, otro):
        """Soporte para el operador +"""
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        """Soporte para el operador =="""
        if not isinstance(otro, Punto):
            return False
        return self.x == otro.x and self.y == otro.y

    def __len__(self):
        """Distancia Manhattan desde el origen."""
        return abs(self.x) + abs(self.y)


# Programa principal
p1 = Punto(3, 4)
p2 = Punto(1, 2)
p3 = Punto(3, 4)

print(f"p1 = {p1}")           # Usa __str__
print(f"repr: {repr(p1)}")    # Usa __repr__
print()

p4 = p1 + p2                  # Usa __add__
print(f"p1 + p2 = {p4}")
print()

print(f"p1 == p2: {p1 == p2}")    # False
print(f"p1 == p3: {p1 == p3}")    # True (mismo x, mismo y)
print()

print(f"len(p1) = {len(p1)}")     # Distancia Manhattan = 3+4 = 7
print(f"len(p2) = {len(p2)}")     # 1+2 = 3