# ============================================================
# Ejemplo 6: Clase Libro
# Autora: Sara García
# Descripción: Ejemplo del material teórico sobre métodos que
#              llaman a otros métodos y __str__.
# ============================================================

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_actual = 0
        self.abierto = False

    def abrir(self):
        if self.abierto:
            return f"{self.titulo} ya esta abierto."
        self.abierto = True
        return f"{self.titulo} ha sido abierto."

    def cerrar(self):
        if not self.abierto:
            return f"{self.titulo} ya esta cerrado."
        self.abierto = False
        return f"{self.titulo} ha sido cerrado."

    def leer(self, num_paginas):
        if not self.abierto:
            return f"No puedes leer: {self.titulo} esta cerrado."
        paginas_restantes = self.paginas - self.pagina_actual
        paginas_a_leer = min(num_paginas, paginas_restantes)
        self.pagina_actual += paginas_a_leer
        if self.pagina_actual >= self.paginas:
            return f"Has leido {paginas_a_leer} paginas y has terminado {self.titulo}."
        return f"Has leido {paginas_a_leer} paginas. Estas en la pagina {self.pagina_actual} de {self.paginas}."

    def reiniciar_lectura(self):
        self.pagina_actual = 0
        return f"Has reiniciado la lectura de {self.titulo}."

    def __str__(self):
        estado = "abierto" if self.abierto else "cerrado"
        return f"{self.titulo} por {self.autor} - {self.pagina_actual}/{self.paginas} paginas - {estado}"


# Programa principal
libro = Libro("El Quijote", "Miguel de Cervantes", 863)

print(libro.leer(50))       # No puede, esta cerrado
print(libro.abrir())
print(libro.leer(50))
print(libro.leer(100))
print(libro.cerrar())
print(libro.abrir())
print(libro.leer(713))      # Termina el libro
print(libro.reiniciar_lectura())
print(libro)