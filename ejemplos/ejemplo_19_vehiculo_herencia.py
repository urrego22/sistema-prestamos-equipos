# ============================================================
# Ejemplo 19: Vehiculo y Coche - Herencia y atributos protegidos
# Autora: Sara García
# Descripción: Ejemplo del material de encapsulación sobre
#              atributos protegidos vs privados en herencia.
# ============================================================

class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido: accesible en subclases
        self.__modelo = modelo   # Privado: NO accesible en subclases

    def info_vehiculo(self):
        return f"Vehiculo: {self._marca} {self.__modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self._puertas = puertas

    def info_coche(self):
        # _marca es protegido: podemos acceder desde la subclase
        info = f"Coche: {self._marca} | Puertas: {self._puertas}"

        # __modelo es privado: NO se puede acceder desde la subclase
        try:
            info += f" | Modelo: {self.__modelo}"
        except AttributeError:
            info += " | (modelo privado: no accesible desde subclase)"

        return info


# Programa principal
vehiculo = Vehiculo("Ford", "F150")
print(vehiculo.info_vehiculo())
print()

coche = Coche("Toyota", "Corolla", 4)

# El metodo heredado de Vehiculo sí puede acceder a __modelo
print(coche.info_vehiculo())

# Pero el metodo propio de Coche no puede
print(coche.info_coche())
print()

# Atributo protegido: accesible desde fuera (por convencion no se hace)
print(f"Marca (protegida): {coche._marca}")

# Atributo privado: no accesible directamente
try:
    print(coche.__modelo)
except AttributeError as e:
    print(f"Error acceso directo a __modelo: {e}")