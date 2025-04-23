# Definir la lista anidada
estudiantes = [
    ["Juan", [85, 90, 78]],
    ["María", [92, 88, 95]],
    ["Carlos", [75, 80, 72]]
]

# Acceder a datos específicos


# Agregar una nueva estudiante con sus notas


# Modificar una nota (Cambiar la segunda nota de Juan)


# Calcular el promedio de cada estudiante

# Eliminar un estudiante (Carlos)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Recorrer la lista de listas usando range
for i in matriz:  # Iterar sobre las filas
    for j in i:  # Iterar sobre las columnas
        print(f"Elemento en [{i}][{j}]: {matriz[i][j]}")
