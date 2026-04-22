import sqlite3

def crear_base():
    # Se conecta (o crea) el archivo inventario.db
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    # Creamos la tabla con los campos EXACTOS del examen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()
    print("¡Base de datos 'inventario.db' y tabla 'productos' creadas!")

if __name__ == '__main__':
    crear_base()