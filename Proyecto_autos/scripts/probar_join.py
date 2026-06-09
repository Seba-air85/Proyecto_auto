#probar_join.py

import sqlite3
import pandas as pd

conn = sqlite3.connect("autos.db")

ventas = pd.read_sql(
    "SELECT * FROM ventas",
    conn
)

print(ventas.head())

conn.close()