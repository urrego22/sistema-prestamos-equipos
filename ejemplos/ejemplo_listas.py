# ============================================================
# Ejemplos de Listas en Python
# Autora: Sara García
# ============================================================

# Una lista es una colección ordenada y modificable de elementos.

# Crear una lista
frutas = ["manzana", "banano", "naranja", "uva"]
print("Lista original:", frutas)

# Acceder a elementos por índice
print("Primera fruta:", frutas[0])
print("Ultima fruta:", frutas[-1])

# Agregar un elemento al final
frutas.append("mango")
print("Despues de append:", frutas)

# Insertar en una posición específica
frutas.insert(1, "pera")
print("Despues de insert en posicion 1:", frutas)

# Eliminar un elemento
frutas.remove("uva")
print("Despues de remove:", frutas)

# Recorrer una lista con for
print("\nRecorriendo la lista:")
for fruta in frutas:
    print(" -", fruta)

# Longitud de la lista
print("\nTotal de frutas:", len(frutas))

# Verificar si un elemento está en la lista
if "mango" in frutas:
    print("El mango esta en la lista")

# Ordenar la lista
frutas.sort()
print("Lista ordenada:", frutas)

# Listas con números
numeros = [5, 3, 8, 1, 9, 2]
print("\nLista de numeros:", numeros)
print("Maximo:", max(numeros))
print("Minimo:", min(numeros))
print("Suma:", sum(numeros))