import matplotlib.pyplot as plt

# Datos para el gráfico
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10, 20, 15, 25, 30]

# Crear el gráfico de barras
plt.bar(categorias, valores, color='red')

# Agregar títulos y etiquetas
titulo = 'Gráfico de Barras en Python'
plt.title(titulo)
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()

# Crear el gráfico de líneas
plt.plot(categorias, valores, marker='o', linestyle='-', color='skyblue')

# Agregar títulos y etiquetas
titulo = 'Gráfico de Líneas en Python'
plt.title(titulo)
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()