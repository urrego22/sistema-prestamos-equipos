# ============================================================
# Sistema de Préstamos de Equipos
# Autora: Sara García
# Descripción: Sistema de gestión de préstamos de equipos
#              de cómputo usando Programación Orientada a Objetos
# ============================================================

from datetime import date


# ============================================================
# CLASE: Prestamo
# Representa un préstamo individual de un equipo.
# Usa encapsulación para proteger los datos del préstamo.
# ============================================================
class Prestamo:

    def __init__(self, usuario, fecha):
        # Atributos privados (encapsulación con __)
        self.__usuario = usuario
        self.__fecha = fecha

    # Métodos getter para acceder a los datos privados
    def get_usuario(self):
        return self.__usuario

    def get_fecha(self):
        return self.__fecha

    # Representación en texto del préstamo
    def __str__(self):
        return f"Usuario: {self.__usuario}  |  Fecha: {self.__fecha}"


# ============================================================
# CLASE: Equipo
# Representa un equipo del inventario.
# Gestiona su disponibilidad e historial de préstamos.
# ============================================================
class Equipo:

    def __init__(self, nombre):
        # Atributos privados
        self.__nombre = nombre
        self.__disponible = True
        self.__historial = []  # Lista de objetos Prestamo

    # Getter del nombre
    def get_nombre(self):
        return self.__nombre

    # Getter de disponibilidad
    def esta_disponible(self):
        return self.__disponible

    # Getter del historial
    def get_historial(self):
        return self.__historial

    # Método para registrar un préstamo
    def prestar(self, usuario):
        if not self.__disponible:
            print(f"  '{self.__nombre}' ya esta prestado.")
            return False
        fecha_hoy = str(date.today())
        nuevo_prestamo = Prestamo(usuario, fecha_hoy)  # Creamos objeto Prestamo
        self.__historial.append(nuevo_prestamo)        # Lo añadimos al historial
        self.__disponible = False                       # Cambiamos estado
        print(f"  Prestamo registrado: '{self.__nombre}' -> {usuario} el {fecha_hoy}")
        return True

    # Método para devolver el equipo
    def devolver(self):
        if self.__disponible:
            print(f"  '{self.__nombre}' no esta prestado.")
            return False
        self.__disponible = True
        print(f"  '{self.__nombre}' devuelto exitosamente.")
        return True

    # Representación en texto del equipo
    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"  - {self.__nombre}: {estado}"


# ============================================================
# CLASE: SistemaPrestamos
# Clase principal que gestiona todo el inventario.
# Contiene la lista de equipos y las operaciones del menú.
# ============================================================
class SistemaPrestamos:

    def __init__(self):
        # Inventario inicial: diccionario de objetos Equipo
        self.__equipos = {
            "Laptop HP":       Equipo("Laptop HP"),
            "Laptop Dell":     Equipo("Laptop Dell"),
            "Tablet Samsung":  Equipo("Tablet Samsung"),
            "Proyector Epson": Equipo("Proyector Epson"),
        }

    # ----------------------------------------------------------
    # Mostrar todos los equipos y su estado
    # ----------------------------------------------------------
    def mostrar_equipos(self):
        print("\n====== INVENTARIO DE EQUIPOS ======")
        for equipo in self.__equipos.values():
            print(equipo)  # Llama al __str__ de Equipo
        print("===================================")

    # ----------------------------------------------------------
    # Registrar un nuevo préstamo
    # ----------------------------------------------------------
    def registrar_prestamo(self):
        print("\n====== REGISTRAR PRESTAMO ======")
        self.mostrar_equipos()

        nombre = input("\nEscribe el nombre exacto del equipo a prestar: ").strip()

        if nombre not in self.__equipos:
            print("  Ese equipo no existe en el sistema.")
            return

        usuario = input("Escribe el nombre del usuario: ").strip()
        self.__equipos[nombre].prestar(usuario)  # Llamamos al método de Equipo

    # ----------------------------------------------------------
    # Devolver un equipo
    # ----------------------------------------------------------
    def devolver_equipo(self):
        print("\n====== DEVOLVER EQUIPO ======")
        nombre = input("Escribe el nombre exacto del equipo a devolver: ").strip()

        if nombre not in self.__equipos:
            print("  Ese equipo no existe en el sistema.")
            return

        self.__equipos[nombre].devolver()  # Llamamos al método de Equipo

    # ----------------------------------------------------------
    # Ver historial completo de préstamos
    # ----------------------------------------------------------
    def ver_historial(self):
        print("\n====== HISTORIAL DE PRESTAMOS ======")
        for nombre, equipo in self.__equipos.items():
            print(f"\n  {nombre}:")
            historial = equipo.get_historial()
            if historial:
                for prestamo in historial:
                    print(f"     {prestamo}")  # Llama al __str__ de Prestamo
            else:
                print("     Sin prestamos registrados.")
        print("\n=====================================")

    # ----------------------------------------------------------
    # Agregar un nuevo equipo al inventario
    # ----------------------------------------------------------
    def agregar_equipo(self):
        print("\n====== AGREGAR NUEVO EQUIPO ======")
        nombre = input("Escribe el nombre del nuevo equipo: ").strip()

        if nombre in self.__equipos:
            print("  Ese equipo ya esta registrado.")
            return

        self.__equipos[nombre] = Equipo(nombre)  # Creamos nuevo objeto Equipo
        print(f"  Equipo '{nombre}' agregado exitosamente.")

    # ----------------------------------------------------------
    # Menú interactivo principal
    # ----------------------------------------------------------
    def menu(self):
        print("\nBienvenido al Sistema de Prestamos de Equipos")
        print("Autora: Sara Garcia")

        while True:
            print("\n======= MENU PRINCIPAL =======")
            print("1. Ver equipos disponibles")
            print("2. Registrar prestamo")
            print("3. Devolver equipo")
            print("4. Ver historial de prestamos")
            print("5. Agregar nuevo equipo")
            print("6. Salir")
            print("==============================")

            opcion = input("Selecciona una opcion (1-6): ").strip()

            if opcion == "1":
                self.mostrar_equipos()
            elif opcion == "2":
                self.registrar_prestamo()
            elif opcion == "3":
                self.devolver_equipo()
            elif opcion == "4":
                self.ver_historial()
            elif opcion == "5":
                self.agregar_equipo()
            elif opcion == "6":
                print("\nHasta luego. Cerrando el sistema...\n")
                break
            else:
                print("  Opcion no valida. Elige un numero del 1 al 6.")


# ============================================================
# Punto de entrada: creamos el sistema y lanzamos el menú
# ============================================================
sistema = SistemaPrestamos()
sistema.menu()