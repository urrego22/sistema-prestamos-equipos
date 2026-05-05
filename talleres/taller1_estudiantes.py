# ============================================================
# Taller 1: Gestión de Estudiantes
# Autora: Sara García
# Descripción: Sistema básico para registrar y consultar
#              información de estudiantes usando listas y diccionarios.
# ============================================================

# Lista de estudiantes (cada uno es un diccionario)
estudiantes = []

def agregar_estudiante(nombre, edad, nota):
    """Agrega un estudiante a la lista."""
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }
    estudiantes.append(estudiante)
    print(f"  Estudiante '{nombre}' registrado.")

def mostrar_estudiantes():
    """Muestra todos los estudiantes registrados."""
    if not estudiantes:
        print("  No hay estudiantes registrados.")
        return
    print("\n====== LISTA DE ESTUDIANTES ======")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']} | Edad: {est['edad']} | Nota: {est['nota']}")
    print("==================================")

def promedio_notas():
    """Calcula y muestra el promedio de notas."""
    if not estudiantes:
        print("  No hay estudiantes para calcular promedio.")
        return
    total = sum(est["nota"] for est in estudiantes)
    promedio = total / len(estudiantes)
    print(f"\nPromedio del grupo: {promedio:.2f}")

def mejor_estudiante():
    """Muestra el estudiante con la nota más alta."""
    if not estudiantes:
        return
    mejor = max(estudiantes, key=lambda e: e["nota"])
    print(f"\nMejor estudiante: {mejor['nombre']} con nota {mejor['nota']}")

# ============================================================
# Programa principal
# ============================================================
agregar_estudiante("Sara García", 20, 4.8)
agregar_estudiante("Carlos López", 22, 3.9)
agregar_estudiante("María Torres", 21, 4.5)
agregar_estudiante("Andrés Ruiz", 23, 3.7)

mostrar_estudiantes()
promedio_notas()
mejor_estudiante()