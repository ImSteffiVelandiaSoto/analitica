import matplotlib.pyplot as plt

# Datos para el gráfico
x = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
y = [10, 20, 15, 25, 30]

# Crear el gráfico de área
plt.fill_between(x, y, color='red', alpha=1)

# Agregar títulos y etiquetas
titulo = 'Crecimiento de Ventas Mensuales'
plt.title(titulo)
plt.xlabel('Meses')
plt.ylabel('Ventas')

# Mostrar el gráfico
plt.show()