# ============================================================
# Ejemplo 12: Clase Empleado
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre @classmethod
#              y atributos de clase como contadores.
# ============================================================

class Empleado:
    # Atributo de clase: cuenta cuantos empleados se han creado
    num_empleados = 0

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.num_empleados += 1  # Incrementa el contador global

    @classmethod
    def desde_salario_anual(cls, nombre, salario_anual):
        """Constructor alternativo: recibe salario anual."""
        salario_mensual = salario_anual / 12
        return cls(nombre, salario_mensual)

    @classmethod
    def obtener_num_empleados(cls):
        """Devuelve cuantos empleados existen."""
        return cls.num_empleados

    def __str__(self):
        return f"{self.nombre} | Salario mensual: ${self.salario:,.2f}"


# Programa principal
print(f"Empleados al inicio: {Empleado.obtener_num_empleados()}")

emp1 = Empleado("Sara Garcia", 3000)
emp2 = Empleado("Carlos Lopez", 2500)
emp3 = Empleado.desde_salario_anual("Maria Torres", 48000)

print()
print(emp1)
print(emp2)
print(emp3)
print()
print(f"Total de empleados creados: {Empleado.obtener_num_empleados()}")