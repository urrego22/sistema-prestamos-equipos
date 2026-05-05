# ============================================================
# Ejemplo 15: Persona con getters y setters
# Autora: Sara García
# Descripción: Ejemplo del material de encapsulación sobre
#              getters y setters para controlar acceso a datos.
# ============================================================

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # --- Getters ---
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    # --- Setters con validacion ---
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")

    def __str__(self):
        return f"{self._nombre} | Edad: {self._edad}"


# Programa principal
ana = Persona("Ana Lopez", 29)

print(ana.get_nombre())
print(ana.get_edad())
print(ana)

# Modificar usando setters
ana.set_nombre("Ana Maria Lopez")
ana.set_edad(30)
print(ana)

# Intentar valores invalidos
try:
    ana.set_edad(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    ana.set_edad(200)
except ValueError as e:
    print(f"Error: {e}")

try:
    ana.set_nombre("")
except ValueError as e:
    print(f"Error: {e}")