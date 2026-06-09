#etl_final.py

import pandas as pd
import sqlite3
import requests

# Leer CSV
vehiculos = pd.read_csv("car details v4.csv")

vehiculos["id_vehiculo"] = range(
    1,
    len(vehiculos) + 1
)

# Leer SQLite
conn = sqlite3.connect("autos.db")

ventas = pd.read_sql(
    "SELECT * FROM ventas",
    conn
)

conn.close()

# JOIN
dataset = ventas.merge(
    vehiculos,
    on="id_vehiculo",
    how="left"
)

print(dataset.head())

# Ejemplo
eur = 0.8647

dataset["precio_usd"] = dataset["Price"] / 100
dataset["precio_eur"] = dataset["precio_usd"] * eur

dataset.to_csv(
    "dataset_final.csv",
    index=False
)
print("dataset_final.csv creado correctamente")
