# ============================================================
# Taller 2: Inventario de Tienda
# Autora: Sara García
# Descripción: Gestión de productos usando diccionarios y tuplas.
#              Permite registrar, buscar y listar productos.
# ============================================================

# Inventario: diccionario donde la clave es el nombre del producto
# y el valor es una tupla inmutable (precio, cantidad)
inventario = {
    "Cuaderno":  (3500, 10),
    "Lapicero":  (1200, 25),
    "Borrador":  (800,  15),
    "Regla":     (2000, 8),
}

def mostrar_inventario():
    """Muestra todos los productos del inventario."""
    print("\n====== INVENTARIO ======")
    print(f"{'Producto':<15} {'Precio':>10} {'Cantidad':>10}")
    print("-" * 38)
    for producto, datos in inventario.items():
        precio, cantidad = datos  # Desempaquetamos la tupla
        print(f"{producto:<15} ${precio:>9} {cantidad:>10}")
    print("========================")

def buscar_producto(nombre):
    """Busca un producto y muestra su información."""
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"\nProducto encontrado: {nombre}")
        print(f"   Precio:   ${precio}")
        print(f"   Cantidad: {cantidad} unidades")
    else:
        print(f"\nProducto '{nombre}' no encontrado.")

def agregar_producto(nombre, precio, cantidad):
    """Agrega un nuevo producto al inventario."""
    if nombre in inventario:
        print(f"  '{nombre}' ya existe en el inventario.")
        return
    inventario[nombre] = (precio, cantidad)  # Guardamos como tupla
    print(f"  Producto '{nombre}' agregado.")

def valor_total():
    """Calcula el valor total del inventario."""
    total = sum(precio * cantidad for precio, cantidad in inventario.values())
    print(f"\nValor total del inventario: ${total:,}")

# ============================================================
# Programa principal
# ============================================================
mostrar_inventario()
buscar_producto("Lapicero")
buscar_producto("Calculadora")
agregar_producto("Calculadora", 25000, 5)
mostrar_inventario()
valor_total()