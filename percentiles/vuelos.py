import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
data = "https://github.com/mwaskom/seaborn-data/raw/master/flights.csv"

# Leer el CSV desde el enlace
df = pd.read_csv(data)

# Verificar los nombres de las columnas para asegurarse de que 'año' y 'mes' existan
print(df.columns)

# Si las columnas tienen otros nombres, renombrarlas a 'año' y 'mes'
df.rename(columns={'year': 'año', 'month': 'mes'}, inplace=True)

# Verificar nuevamente los nombres de las columnas
print(df.columns)

# Convertir el año y mes en un solo índice de fecha
df['date'] = pd.to_datetime(df['año'].astype(str) + '-' + df['mes'], format='%Y-%B')
df.set_index('date', inplace=True)

print(df)

# Eliminar las columnas originales de año y mes
df.drop(columns=['año', 'mes'], inplace=True)
print(df)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Estadísticas básicas
print("\nEstadísticas básicas:")
print(df.describe())

# 📊 **Cálculo de percentiles**
percentiles = [0.1, 0.25, 0.5, 0.75,0.9]  # 25%, 50%, 75%
percentile_values = df['passengers'].quantile(percentiles)
#print(percentile_values)

# Crear DataFrame con los percentiles
percentile_df = pd.DataFrame({
    'Percentile': [f'{int(p*100)} %' for p in percentiles],
    'Value': percentile_values
})

# Mostrar los percentiles
print("\nPercentiles Calculados:")
print(percentile_df)
