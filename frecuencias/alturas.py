import pandas as pd
import mat
# Datos de alturas y frecuencias
datos = {
    "Altura (m)": [1.45, 1.68, 1.70, 1.73, 1.75, 1.80, 1.82],
    "Frecuencia (f)": [3, 5, 6, 2, 2, 1, 1]
}
# Crear DataFrame
df = pd.DataFrame(datos)
#Calcular la Frecuencia Acumulada
df["Frecuencia Acumulada (F)"] = df["Frecuencia (f)"].cumsum()
# Calcular la Frecuencia Relativa    /// si es diccionario se debe hacer con sum
df["Frecuencia Relativa (fr)"] = df["Frecuencia (f)"] / df["Frecuencia (f)"].sum()
# Calcular la Frecuencia Relativa en porcentaje
df["Frecuencia Relativa (%)"] = df["Frecuencia Relativa (fr)"] * 100
df["FRA"]= df["Frecuencia Relativa (%)"].cumsum()
print(df)
