calificaciones = (85, 90, 78, 92, 88, 76, 95, 89, 78, 90)


# 1. Determinar la cantidad de calificaciones
cantidad= len(calificaciones)
print(f" La cantidad de calificaciones es: {cantidad}")

# 2. Encontrar la calificación más alta y la más baja
maxCalificacion= max(calificaciones)
minCalificacion= min(calificaciones)
print(f"La calificación maxima es: {maxCalificacion}  y la minima  {minCalificacion}")

# 3. Calcular el promedio de las calificaciones
promedio=sum(calificaciones)/cantidad
print(f"El promedio de las notas es {promedio}")

# 4. Contar cuántas veces aparece una calificación específica (por ejemplo, 90)
repeticiones= calificaciones.count(1)
print(f"El numero 1 se encuentra {repeticiones} veces")

# 5. Encontrar el índice de la primera aparición de una calificación específica (por ejemplo, 78)
indice=calificaciones.index(78)
print(f"La calificación aparece en el indice \n  {indice} por primera vez")

# 6. Desempaquetado de tupla (ejemplo con las tres primeras calificaciones)

primera, segunda, tercera, *resto= calificaciones

print(primera)
print(segunda)
print(tercera)
print(resto)