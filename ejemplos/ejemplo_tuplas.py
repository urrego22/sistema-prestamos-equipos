# ============================================================
# Ejemplos de Tuplas en Python
# Autora: Sara García
# ============================================================

# Una tupla es como una lista pero INMUTABLE (no se puede modificar).
# Se usa cuando los datos no deben cambiar.

# Crear una tupla
coordenadas = (4.7110, -74.0721)  # Coordenadas de Bogotá
print("Coordenadas:", coordenadas)
print("Latitud:", coordenadas[0])
print("Longitud:", coordenadas[1])

# Tupla con datos de una persona
persona = ("Sara García", 18, "Medellin")
nombre, edad, ciudad = persona  # Desempaquetado
print("\nNombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# Las tuplas no se pueden modificar
# persona[0] = "Otro nombre"  # <- Esto daria error

# Tupla de un solo elemento (necesita coma)
un_elemento = ("Python",)
print("\nTupla de un elemento:", un_elemento)

# Recorrer una tupla
colores = ("rojo", "verde", "azul")
print("\nColores disponibles:")
for color in colores:
    print(" -", color)

# Verificar si algo está en la tupla
if "verde" in colores:
    print("\nEl verde esta en los colores")

# Longitud
print("Total de colores:", len(colores))

# Tuplas como registros inmutables (como en el proyecto de prestamos)
prestamo = ("Carlos Lopez", "2025-05-05")
print("\nPrestamo registrado:")
print(f"  Usuario: {prestamo[0]}")
print(f"  Fecha:   {prestamo[1]}")