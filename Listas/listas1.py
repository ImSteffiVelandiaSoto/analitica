# Definir una lista con diferentes tipos de datos
mi_lista = [10, "Python", 3.14, True, "Código"]

# Acceder a elementos específicos
print("primer elemento", mi_lista[0])
print("Ultimo elemento", mi_lista[-1])

# Modificar un elemento
mi_lista[1]="programación"
print("Lista despues de modificada: ", mi_lista)

# Agregar y eliminar elementos
mi_lista.append("Nuevo")
print("Lista despues agregado: ", mi_lista)

mi_lista.remove(3.14)
print("Lista despues eliminado: ", mi_lista)

#eliminar la ultima posicion
mi_lista.pop()
print("Lista pop: ", mi_lista)


# Recorrer la lista con un bucle
print("Elementos de la lista:")
for elemento in mi_lista:
    print("-", elemento)

# Aplicar list comprehension: obtener longitud de cada palabra
palabras=["Python", "Java", "C++"]
longitudes=[len(palabra)  for palabra in palabras]
print("Estas son las longitudes de las palabras: ", longitudes)

# Filtrar solo números de una lista mixta
mixta = [10, "Python", 3.14, "False", "Código"]
numeros=[num for num in mixta if isinstance(num, (int, float))]
print("Estos son los numeros de la lista original: ", numeros)