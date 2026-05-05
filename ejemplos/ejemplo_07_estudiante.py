# ============================================================
# Ejemplo 7: Clase Estudiante
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre atributos
#              de instancia vs atributos de clase.
# ============================================================

class Estudiante:
    # Atributo de clase: compartido por TODOS los objetos
    universidad = "SENA"

    def __init__(self, nombre, edad):
        # Atributos de instancia: únicos para cada objeto
        self.nombre = nombre
        self.edad = edad
        self.activo = True

    def presentarse(self):
        estado = "activo" if self.activo else "inactivo"
        return f"{self.nombre} ({self.edad} anos) - {self.universidad} - {estado}"

    def desactivar(self):
        self.activo = False
        return f"{self.nombre} ha sido desactivado."


# Programa principal
est1 = Estudiante("Sara Garcia", 18)
est2 = Estudiante("Carlos Lopez", 22)
est3 = Estudiante("Maria Torres", 20)

# Todos comparten el atributo de clase
print(est1.universidad)
print(est2.universidad)
print(Estudiante.universidad)   # Tambien se puede acceder desde la clase
print()

# Cada uno tiene sus propios atributos de instancia
print(est1.presentarse())
print(est2.presentarse())
print(est3.presentarse())
print()

# Si cambia el atributo de clase, afecta a todos
Estudiante.universidad = "SENA Regional Medellin"
print(est1.universidad)
print(est2.universidad)
print()

# Desactivar un estudiante (solo afecta a ese objeto)
print(est3.desactivar())
print(est3.presentarse())
print(est1.presentarse())   # est1 sigue activo