# etl_final.py

import pandas as pd
import sqlite3
import requests
from pathlib import Path

print("Iniciando proceso ETL...")

BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "data" / "raw" / "car details v4.csv"
db_path = BASE_DIR / "data" / "raw" / "autos.db"

vehiculos = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)
# EXTRACT - CSV
try:
    print(f"CSV cargado correctamente ({len(vehiculos)} registros)")
except FileNotFoundError:
    print("Error: no se encontró el archivo 'car details v4.csv'")
    exit()

# Validar columnas necesarias
print("\nColumnas encontradas en el CSV:")
print(vehiculos.columns.tolist())

columnas_requeridas = [
    "Make",
    "Model",
    "Price",
    "Year",
    "Fuel Type",
    "Transmission"
]

for columna in columnas_requeridas:
    if columna not in vehiculos.columns:
        print(f"Error: falta la columna '{columna}'")
        exit()

# Crear id para relacionar con ventas
vehiculos["id_vehiculo"] = range(
    1,
    len(vehiculos) + 1
)

# EXTRACT - SQLITE
try:
    conn = sqlite3.connect(db_path)

    ventas = pd.read_sql(
        "SELECT * FROM ventas",
        conn
    )

    conn.close()

    print(f"Base de datos cargada ({len(ventas)} ventas)")

except Exception as e:
    print(f"Error al leer SQLite: {e}")
    exit()

# EXTRACT - API
try:
    url = "https://open.er-api.com/v6/latest/USD"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:

        data = response.json()

        eur = data["rates"]["EUR"]

        print(f"Tipo de cambio USD -> EUR obtenido desde API: {eur}")

    else:
        raise Exception(
            f"Respuesta HTTP {response.status_code}"
        )

except Exception as e:

    print(
        f"No se pudo obtener el tipo de cambio desde la API: {e}"
    )

    eur = 0.8647

    print(
        f"Usando valor de respaldo: {eur}"
    )

# TRANSFORM
dataset = ventas.merge(
    vehiculos,
    on="id_vehiculo",
    how="left"
)

print("JOIN realizado correctamente")

# Conversión de moneda

if "Price" not in dataset.columns:
    print("Error: no existe la columna 'Price'")
    exit()

dataset["precio_usd"] = dataset["Price"] / 100

dataset["precio_eur"] = (
    dataset["precio_usd"] * eur
)

# LOAD
try:

    output_path = BASE_DIR / "data" / "processed" / "dataset_final.csv"

    dataset.to_csv(
        output_path,
        index=False
    )

    print(
        f"dataset_final.csv creado correctamente ({len(dataset)} registros)"
    )

except Exception as e:

    print(
        f"Error al guardar dataset_final.csv: {e}"
    )

print("Proceso ETL finalizado")