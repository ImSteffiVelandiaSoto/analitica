import pandas as pd
import numpy as np
from faker import Faker
from pandasgui import show

# Generador de datos falsos
fake = Faker('es_CO')

# Generar datos
np.random.seed(42)
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

# Mostrar en PandasGUI
show(df_clientes)