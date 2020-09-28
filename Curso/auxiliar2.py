# -*- coding: utf-8 -*-
import sqlite3

# Conexión y cursor a la base de datos
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Creo la tabla
cursor.execute("""CREATE TABLE currency
 (ID integer primary key, name text, symbol text)""")

# Inserto datos de monedas
cursor.execute("INSERT INTO currency VALUES (1, 'Peso (ARG)', '$')")
cursor.execute("INSERT INTO currency VALUES (2, 'Dólar', 'U$S')")

# Guardo los cambios
conn.commit()

# Consulto todas las monedas
query = "SELECT * FROM currency"

# Busco el resultado
currencies = cursor.execute(query).fetchall()
print(currencies)

# Cierro la conexión a la base de datos
conn.close()