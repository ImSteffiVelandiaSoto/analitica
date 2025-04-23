import pandas as pd
from collections import Counter
# Datos de horas de estudio
horas_estudio = [2, 5, 10, 7, 7, 3, 3, 3, 1, 1, 2, 8, 10, 10, 2, 1, 3, 3, 3, 15]
# Contar las frecuencias
conteo = Counter(horas_estudio)
print(conteo)
# Crear DataFrame
df = pd.DataFrame(sorted(conteo.items()), columns=["Horas de Estudio", "Frecuencia (f)"])
# Calcular la Frecuencia Acumulada
df["Frecuencia Acumulada (F)"] = df["Frecuencia (f)"].cumsum()
# Calcular la Frecuencia Relativa     /// si es lista se utiliza la funcion Len
df["Frecuencia Relativa (fr)"] = df["Frecuencia (f)"] / len(horas_estudio)
# Calcular la Frecuencia Relativa en porcentaje
df["Frecuencia Relativa (%)"] = (df["Frecuencia Relativa (fr)"]) * 100
df["FRA"] = df["Frecuencia Relativa (%)"].cumsum()
print(df)

