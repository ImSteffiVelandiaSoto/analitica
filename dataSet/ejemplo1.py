import pandas as pd
import numpy as np
from faker import Faker

# Inicializamos Faker y configuramos datos base
faker = Faker()
np.random.seed(42)
n = 10000

# Datos base
ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']
productos = ['Laptop', 'Tablet', 'Celular', 'Monitor', 'Teclado', 'Mouse']

# Creamos el dataset
data = {
    "ID_Venta": np.arange(1, n + 1), #incrementa de 1 en 1
    "Fecha": [faker.date_between(start_date='-1y', end_date='today') for _ in range(n)], #genera fechas de hace un año atras hasta hoy
    "Cliente": [faker.name() for _ in range(n)], #Nombres Fakes
    "Ciudad": np.random.choice(ciudades, n), #Ciudades del array escoje 1 al azar
    "Producto": np.random.choice(productos, n), #Productos del array escoje 1 al azar
    "Cantidad": np.random.randint(1, 10, size=n), #generar aleatorios numero del 1 a 10
    "Precio_Unitario": np.random.randint(100000, 2000000, size=n) # generar numeros aleatorios de 100000 a 2000000
}

df = pd.DataFrame(data)


# Añadimos la columna Total
df["Total"] = df["Cantidad"] * df["Precio_Unitario"]



# ----------------------------------------
# FUNCIONES APLICADAS AL DATASET
# ----------------------------------------

# 1. Ver primeras filas
print("Primeras filas del dataset:")
print(df.head())

#print(df)


# 2. Información general del DataFrame
print("\nInformación del DataFrame:")
print(df.info())


# 3. Estadísticas descriptivas
print("\nEstadísticas del dataset:")
print(df.describe())

# 4. Total de ventas por ciudad
print("\nTotal de ventas por ciudad:")
print(df.groupby("Ciudad")["Total"].sum())


# 5. Producto más vendido (por cantidad total)
print("\nProducto más vendido por cantidad total:")
print(df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False))


# 6. Ventas mayores a $5 millones
ventas_altas = df[df["Total"] > 5000000]
print("\nVentas mayores a $5 millones:")
print(ventas_altas.head())


# 7. Agregar una columna "Clasificación"
df["Clasificación"] = df["Total"].apply(lambda x: "Alta" if x > 5_000_000 else "Normal")
print("\nClasificación de las ventas (Alta o Normal):")
print(df["Clasificación"].value_counts())


# 8. Ordenar por Total (descendente)
ventas_ordenadas = df.sort_values(by="Total", ascending=False)
print("\nTop 5 ventas más altas:")
print(ventas_ordenadas.head(10))

# 9. Revisar si hay datos nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

#10. Guardar el dataset procesado en un archivo CSV (opcional)
df.to_csv("ventas_procesadas.csv", index=False)
