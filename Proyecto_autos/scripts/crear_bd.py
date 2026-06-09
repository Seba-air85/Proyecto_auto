#crear_bd.py

import sqlite3

# Crear conexión
conn = sqlite3.connect("autos.db")

cursor = conn.cursor()

# Tabla clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT,
    telefono TEXT,
    ciudad TEXT,
    fecha_registro DATE
)
""")

# Tabla sucursales
cursor.execute("""
CREATE TABLE IF NOT EXISTS sucursales (
    id_sucursal INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    ciudad TEXT,
    region TEXT
)
""")

# Tabla vendedores
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendedores (
    id_vendedor INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    id_sucursal INTEGER,
    FOREIGN KEY(id_sucursal) REFERENCES sucursales(id_sucursal)
)
""")

# Tabla ventas
cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_vehiculo INTEGER,
    id_vendedor INTEGER,
    fecha_venta DATE,
    precio_venta REAL,
    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY(id_vendedor) REFERENCES vendedores(id_vendedor)
)
""")

conn.commit()
conn.close()

print("Base de datos creada correctamente")