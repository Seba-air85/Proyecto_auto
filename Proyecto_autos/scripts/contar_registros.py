#contar_registros.py

import sqlite3

conn = sqlite3.connect("autos.db")
cursor = conn.cursor()

tablas = [
    "clientes",
    "sucursales",
    "vendedores",
    "ventas"
]

for tabla in tablas:

    cursor.execute(
        f"SELECT COUNT(*) FROM {tabla}"
    )

    total = cursor.fetchone()[0]

    print(f"{tabla}: {total}")

conn.close()