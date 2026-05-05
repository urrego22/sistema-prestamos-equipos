# ============================================================
# Ejemplos de Diccionarios en Python
# Autora: Sara García
# ============================================================

# Un diccionario guarda datos en pares clave:valor.
# Es como un directorio: buscas por nombre y obtienes info.

# Crear un diccionario
estudiante = {
    "nombre": "Sara García",
    "edad": 18,
    "ciudad": "Medellin",
    "carrera": "Tecnologia software"
}
print("Estudiante:", estudiante)

# Acceder a un valor por su clave
print("\nNombre:", estudiante["nombre"])
print("Ciudad:", estudiante["ciudad"])

# Modificar un valor
estudiante["edad"] = 18
print("Edad actualizada:", estudiante["edad"])

# Agregar una clave nueva
estudiante["semestre"] = 3
print("Con semestre:", estudiante)

# Eliminar una clave
del estudiante["semestre"]
print("Sin semestre:", estudiante)

# Recorrer claves y valores
print("\nDatos del estudiante:")
for clave, valor in estudiante.items():
    print(f"  {clave}: {valor}")

# Verificar si una clave existe
if "nombre" in estudiante:
    print("\nLa clave 'nombre' existe")

# Diccionario anidado (como en el proyecto de prestamos)
inventario = {
    "Laptop HP": {
        "disponible": True,
        "prestamos": []
    },
    "Tablet Samsung": {
        "disponible": False,
        "prestamos": [("Ana", "2025-05-01")]
    }
}

print("\nInventario de equipos:")
for equipo, info in inventario.items():
    estado = "Disponible" if info["disponible"] else "Prestado"
    print(f"  {equipo}: {estado}")