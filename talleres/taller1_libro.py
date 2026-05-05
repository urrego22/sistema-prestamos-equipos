# ============================================================
# Taller 1: Clases y Objetos en Python
# Autora: Sara García
# Descripción: Clase Libro para gestionar información básica
#              de libros en una biblioteca.
# ============================================================


class Libro:

    def __init__(self, titulo, autor, paginas):
        """
        Constructor de la clase Libro.

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            paginas (int): Número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True  # Inicialmente el libro está disponible

    def prestar(self):
        """Presta el libro si está disponible."""
        if not self.disponible:
            return f"'{self.titulo}' no está disponible, ya fue prestado."
        self.disponible = False
        return f"'{self.titulo}' ha sido prestado exitosamente."

    def devolver(self):
        """Devuelve el libro si estaba prestado."""
        if self.disponible:
            return f"'{self.titulo}' ya estaba disponible en la biblioteca."
        self.disponible = True
        return f"'{self.titulo}' ha sido devuelto exitosamente."

    def informacion(self):
        """Devuelve una cadena con toda la información del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return (
            f"Titulo:      {self.titulo}\n"
            f"Autor:       {self.autor}\n"
            f"Paginas:     {self.paginas}\n"
            f"Disponible:  {estado}"
        )


# ============================================================
# Prueba de la clase Libro
# ============================================================
def main():
    # Crear dos objetos libro diferentes
    libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
    libro2 = Libro("Cien anos de soledad", "Gabriel Garcia Marquez", 471)

    # Mostrar información inicial de los libros
    print("=== Informacion inicial de los libros ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())
    print()

    # Prestar los libros
    print("=== Prestamo de libros ===")
    print(libro1.prestar())
    print(libro2.prestar())
    print()

    # Intentar prestar un libro ya prestado
    print("=== Intento de prestamo de libro ya prestado ===")
    print(libro1.prestar())
    print()

    # Mostrar información después del préstamo
    print("=== Informacion despues del prestamo ===")
    print(libro1.informacion())
    print()

    # Devolver un libro
    print("=== Devolucion de libros ===")
    print(libro1.devolver())
    print()

    # Intentar devolver un libro ya disponible
    print("=== Intento de devolucion de libro ya disponible ===")
    print(libro1.devolver())
    print()

    # Mostrar información final
    print("=== Informacion final de los libros ===")
    print(libro1.informacion())
    print()
    print(libro2.informacion())


if __name__ == "__main__":
    main()