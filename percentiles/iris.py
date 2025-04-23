import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandasgui import show


# Configuración de gráficos
#sns.set(style="whitegrid")

# Cargar un conjunto de datos de ejemplo
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
data = pd.read_csv(url)

df=pd.DataFrame(data)

show(df)

"""
# Mostrar las primeras filas del conjunto de datos
print("primeras 5 filas")
print(data.head(10))

# Definir los percentiles que queremos calcular
percentiles = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]  # 25%, 50%, 75%

# Calcular percentiles
percentile_values = np.percentile(data['sepal_width'], [p * 100 for p in percentiles])


# Crear DataFrame con los percentiles
percentile_df = pd.DataFrame({
    'Percentile': [f'{int(p*100)}%' for p in percentiles],
    'Value': percentile_values
})

# Imprimir los valores percentiles
print("Percentiles Calculados:")
print(percentile_df)



#Un histograma muestra la distribución de los datos.
plt.figure(figsize=(10, 6))
sns.histplot(data['sepal_width'], bins=3, kde=False, color='blue')
plt.title('Histograma de anchura del Sépalo')
plt.xlabel('Anchura del Sépalo (cm)')
plt.ylabel('Frecuencia')
plt.show()



#Si deseas visualizar la relación entre dos variables, usa un gráfico de dispersión.
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['petal_length'], y=data['petal_width'], hue=data['species'])
plt.title('Gráfico de Dispersión: Longitud vs. Ancho del Sépalo')
plt.xlabel('Longitud del Sépalo (cm)')
plt.ylabel('Ancho del Sépalo (cm)')
plt.legend(title='Especie')
plt.show()

"""