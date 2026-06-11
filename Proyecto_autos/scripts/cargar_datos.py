#cargar_datos.py

import sqlite3
import random
from faker import Faker

fake = Faker("es_ES")

conn = sqlite3.connect("autos.db")
cursor = conn.cursor()

# -------------------------
# SUCURSALES
# -------------------------

sucursales = [
    ("Santiago Centro", "Santiago", "Metropolitana"),
    ("Providencia", "Santiago", "Metropolitana"),
    ("Viña del Mar", "Viña del Mar", "Valparaíso"),
    ("Concepción", "Concepción", "Biobío"),
    ("La Serena", "La Serena", "Coquimbo")
]

cursor.executemany("""
INSERT INTO sucursales (nombre, ciudad, region)
VALUES (?, ?, ?)
""", sucursales)

# -------------------------
# VENDEDORES
# -------------------------

for _ in range(15):
    cursor.execute("""
    INSERT INTO vendedores
    (nombre, id_sucursal)
    VALUES (?, ?)
    """, (
        fake.name(),
        random.randint(1, 5)
    ))

# -------------------------
# CLIENTES
# -------------------------

for _ in range(200):
    cursor.execute("""
    INSERT INTO clientes
    (nombre, email, telefono, ciudad, fecha_registro)
    VALUES (?, ?, ?, ?, ?)
    """, (
        fake.name(),
        fake.email(),
        fake.phone_number(),
        random.choice([
            "Santiago",
            "Valparaíso",
            "Concepción",
            "La Serena",
            "Antofagasta"
        ]),
        fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    ))

# -------------------------
# VENTAS
# -------------------------

for _ in range(500):

    id_cliente = random.randint(1, 200)
    id_vendedor = random.randint(1, 15)

    # IMPORTANTE:
    # corresponde a un vehículo del CSV
    id_vehiculo = random.randint(1, 2059)

    precio_venta = random.randint(
        300000,
        2500000
    )

    cursor.execute("""
    INSERT INTO ventas
    (
        id_cliente,
        id_vehiculo,
        id_vendedor,
        fecha_venta,
        precio_venta
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        id_cliente,
        id_vehiculo,
        id_vendedor,
        fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        precio_venta
    ))

conn.commit()
conn.close()

print("Datos cargados correctamente")