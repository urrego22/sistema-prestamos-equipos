# ============================================================
# Ejemplo 9: Clase Calculadora
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre métodos que
#              devuelven valores, incluyendo diccionarios.
# ============================================================

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: Division por cero."
        return a / b

    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {"suma": 0, "promedio": 0, "minimo": None, "maximo": None}
        return {
            "suma":     sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo":   min(numeros),
            "maximo":   max(numeros)
        }


# Programa principal
calc = Calculadora()

print(f"5 + 3 = {calc.sumar(5, 3)}")
print(f"10 - 4 = {calc.restar(10, 4)}")
print(f"6 * 7 = {calc.multiplicar(6, 7)}")
print(f"10 / 2 = {calc.dividir(10, 2)}")
print(f"10 / 0 = {calc.dividir(10, 0)}")
print()

numeros = [4, 7, 2, 9, 5]
stats = calc.calcular_estadisticas(numeros)
print(f"Numeros: {numeros}")
print(f"Suma:     {stats['suma']}")
print(f"Promedio: {stats['promedio']}")
print(f"Minimo:   {stats['minimo']}")
print(f"Maximo:   {stats['maximo']}")