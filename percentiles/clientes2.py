import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker

# Configuración de Faker en español colombiano
fake = Faker('es_CO')
np.random.seed(42)

# Generar datos de clientes
num_clientes = 100
generos = ['Masculino', 'Femenino', 'Otro']
ciudades = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga', 'Manizales']

data = {
    'ID': [f'C-{i+1:04d}' for i in range(num_clientes)],
    'Nombre': [fake.name() for _ in range(num_clientes)],
    'Edad': np.random.randint(18, 70, num_clientes),
    'Ciudad': np.random.choice(ciudades, num_clientes),
    'Correo': [fake.email() for _ in range(num_clientes)],
    'Género': np.random.choice(generos, num_clientes),
    'Satisfacción (1-10)': np.random.randint(1, 11, num_clientes)
}

df_clientes = pd.DataFrame(data)

# Título en la app
st.title("📊 Visualización de Datos de Clientes")

# Mostrar el dataframe completo
st.dataframe(df_clientes)

# Filtro opcional por ciudad
ciudad_filtro = st.selectbox("Filtrar por ciudad:", ["Todas"] + ciudades)
if ciudad_filtro != "Todas":
    df_filtrado = df_clientes[df_clientes["Ciudad"] == ciudad_filtro]
    st.dataframe(df_filtrado)
else:
    st.dataframe(df_clientes)

# Mostrar resumen estadístico
if st.checkbox("Mostrar resumen estadístico"):
    st.write(df_clientes.describe())
