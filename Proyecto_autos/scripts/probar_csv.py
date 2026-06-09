#probar_csv.py

import pandas as pd

df = pd.read_csv("car details v4.csv")

# Crear ID único para cada vehículo
df["id_vehiculo"] = range(1, len(df) + 1)

print(df[["id_vehiculo", "Make", "Model", "Price"]].head())

# 1. Leer CSV
df = pd.read_csv("car details v4.csv")

# 2. Agregar ID
df["id_vehiculo"] = range(1, len(df) + 1)

# 3. Hacer transformaciones
# limpieza, nulos, etc.

# 4. Guardar o usar los datos