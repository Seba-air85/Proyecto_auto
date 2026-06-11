#verificar_bd.py

import sqlite3

conn = sqlite3.connect("autos.db")

cursor = conn.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

for tabla in cursor.fetchall():
    print(tabla[0])

conn.close()