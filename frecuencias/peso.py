import pandas as pd

# Datos de la tabla de pesos y sus frecuencias absolutas
pesos = ["50-60", "60-70", "70-80", "80-90", "90-100", "100-110", "110-120"]
frecuencia_absoluta = [8, 10, 16, 14, 10, 5, 2]

# Crear DataFrame
df_pesos = pd.DataFrame({
    "Intervalo de Peso (kg)": pesos,
    "Frecuencia Absoluta (f)": frecuencia_absoluta
})

# Calcular la Frecuencia Acumulada
df_pesos["Frecuencia Acumulada (F)"] = df_pesos["Frecuencia Absoluta (f)"].cumsum()

# Calcular la Frecuencia Relativa
total_datos = sum(frecuencia_absoluta)
df_pesos["Frecuencia Relativa (fr)"] = (df_pesos["Frecuencia Absoluta (f)"] / total_datos)*100

# Calcular la Frecuencia Relativa Acumulada
df_pesos["Frecuencia Relativa Acumulada (Fr)"] = (df_pesos["Frecuencia Relativa (fr)"].cumsum())*100

# Mostrar la tabla generada
print(df_pesos)