import pandas as pd
import numpy as np

# Crear el DataFrame con datos sucios
data = {
    'ID_venta': [101, 102, 103, 104, 105, 106, 106, 107, 108, None],
    'Fecha': ['2024-03-01', '03/02/2024', 'Mar 03, 2024', '2024/04/04', None, '2024-05-06', '2024-05-06', '06-07-2024', '2024/08/08', '2024-09-09'],
    'Cliente': ['Juan Pérez', 'Ana López', None, 'Carlos Díaz', 'sin nombre', 'Luis Torres', 'Luis Torres', 'Marta Gómez', 'José García', 'Ana López'],
    'Producto': ['Laptop', 'Celular', 'Laptop', 'Tablet', 'Monitor', 'Celular', 'Celular', 'sin info', 'Laptop', 'Monitor'],
    'Cantidad': [1, 2, 'tres', None, 5, 1, 1, 2, 'dos', 1],
    'Precio_unitario': ['$1200', '$800', '$1500', '$600', '$300', '$700', '$700', '$200', '$1300', '$300'],
    'Total': [1200, 1600, None, 2400, 1500, None, 700, 400, 2600, 300]
}

df = pd.DataFrame(data)
print("Dataset original:")
print(df)
#--------- Limpieza-------------
#  Eliminar filas con ID_venta nulo y eliminar duplicados
df = df.dropna(subset=['ID_venta']).drop_duplicates()

#  Normalizar la columna 'Fecha' a formato YYYY-MM-DD
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')

#  Reemplazar valores incorrectos en la columna 'Cliente'
df['Cliente'] = df['Cliente'].replace({None: 'Desconocido', 'sin nombre': 'Desconocido'})

#  Reemplazar valores incorrectos en 'Producto'
df['Producto'] = df['Producto'].replace({'sin info': 'Desconocido'})

#  Convertir la columna 'Cantidad' a número (reemplazando palabras)
valores_cantidad = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}
df['Cantidad'] = df['Cantidad'].replace(valores_cantidad)
df['Cantidad'] = pd.to_numeric(df['Cantidad'], errors='coerce').fillna(1)  # Si hay valores nulos, poner 1

#  Limpiar la columna 'Precio_unitario' y convertirla a número
df['Precio_unitario'] = df['Precio_unitario'].str.replace('$', '', regex=False).astype(float)

#  Calcular correctamente la columna 'Total' donde haya valores nulos o incorrectos
df['Total'] = df['Cantidad'] * df['Precio_unitario']

#  Normalizar los nombres de las columnas
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 9 Verificar los cambios realizados


print("Dataset limpio:")
print(df)
df.to_csv('datos_limpios.csv', index=False)
#ubi especifica
#df.to_csv(r'C:\Users\steff\OneDrive\Documentos\ventas_limpias.csv', index=False)

#google collab
#from google.colab import files
#files.download('ventas_limpias.csv')


#--------- Analisis-------------


# Total de ventas por cliente
ventas_por_cliente = df.groupby('cliente')['total'].sum()
print("Total de ventas por cliente:\n", ventas_por_cliente)

# roducto más vendido
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
print("Producto más vendido:", producto_mas_vendido)

# Total de ingresos generados
total_ingresos = df['total'].sum()
print(" Total de ingresos generados:", total_ingresos)