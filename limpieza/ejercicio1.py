"""import pandas as pd
import numpy as np

# Crear el DataFrame con datos sucios
data = {
    'ID trabajador': [1, 2,2, 3, 4, 5, 5],
    'Nombre': ['Ana López', 'Juan Pérez','Juan Pérez', np.nan, 'María Gómez', 'Pedro Díaz', 'Pedro Díaz'],
    'Edad': ['25', '30','30', 'veintidós', np.nan, '40', '40'],
    'Email': ['ana@email.com', 'juan@email.com','juan@email.com', 'sin email', 'maria@email.com', None, 'pedro@email.com'],
    'Salario': ['3000$', '4000$','4000$', '2500$', np.nan, '5000$', '5000$']
}

df = pd.DataFrame(data)
print(df)

### 1. Eliminar duplicados ### drop_duplicates
#print("Eliminar los datos")
df = df.drop_duplicates()
#print(df)

### 2. Manejar valores nulos ###  fillna
 # Reemplazar nombres nulos
#print("Este es el df  sin np.nan")
df['Nombre'] =df['Nombre'].fillna('Desconocido')
#print(df)
 # Corregir edad mal escrita ### replace
#print("Este es es df con valor numerico 22")
df['Edad']=df['Edad'].replace('veintidós', '22')
#print(df)

 # Convertir Edad a número pandas.to_numeric
df['Edad']=pd.to_numeric(df['Edad'], errors='coerce')
#print(df)

 # Quitar $ y convertir a número
#print("df din $ en salario y en float")
df['Salario']= df['Salario'].str.replace('$', '').astype(float) 
#print(df)

# Convertir "sin email" en NaN ## replace
#print("df eliminar el Sin Email")
df['Email']=df['Email'].replace('sin email', np.nan) # sin email
# Rellenar emails faltantes
df['Email']=df['Email'].fillna('No proporcionado')
#print(df)
 

### 3. Normalizar nombres de columnas ###
 # Convertir nombres de columnas a minúsculas y sin espacios
df.columns=df.columns.str.lower().str.replace(' ', '-')
print(df)

### Mostrar el resultado ###
"""
import pandas as pd

# Datos de ejemplo
data = {
    'Vendedor': ['Ana', 'Carlos', 'Ana', 'Carlos', 'Ana', 'Beatriz'],
    'Región': ['Norte', 'Sur', 'Norte', 'Sur', 'Centro', 'Centro'],
    'Ventas': [100, 200, 150, 250, 300, 180]
}

df = pd.DataFrame(data)

# Crear tabla dinámica
tabla_pivot = pd.pivot_table(df, values='Ventas', index='Vendedor', columns='Región', aggfunc='sum', fill_value=0)

print(tabla_pivot)
